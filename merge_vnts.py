# merge_vnts.py
import os
import shutil
import random
from master_map import master_map, unified_classes

# Paths
vnts_base_dir = r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\VNTS'
chinese_base_dir = r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\Chinese'
indian_base_dir = r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\Indian'
output_dir = r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\GSTRB\merged_dataset'

# Create output folders
for split in ['train', 'val', 'test']:
    os.makedirs(os.path.join(output_dir, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels', split), exist_ok=True)

# Process datasets
datasets = [
    ('vnts', vnts_base_dir, ['train', 'valid', 'test']),
    ('chinese', chinese_base_dir, ['train', 'val', 'test']),  # Adjust splits based on your folder structure
    ('indian', indian_base_dir, ['train', 'val', 'test'])
]

processed_count = 0
for dataset_name, base_dir, splits in datasets:
    for split in splits:
        image_dir = os.path.join(base_dir, split, 'images')
        label_dir = os.path.join(base_dir, split, 'labels')
        target_split = 'train' if split == 'train' else 'val' if split == 'valid' else 'test'
        
        if not os.path.exists(image_dir):
            print(f"Warning: {image_dir} does not exist. Skipping.")
            continue
        
        for img_filename in os.listdir(image_dir):
            if not img_filename.endswith(('.png', '.jpg')):
                continue
            
            img_path = os.path.join(image_dir, img_filename)
            label_path = os.path.join(label_dir, img_filename.replace('.png', '.txt').replace('.jpg', '.txt'))
            
            if not os.path.exists(label_path):
                print(f"Warning: Label not found for {img_filename}. Skipping.")
                continue
            
            with open(label_path, 'r') as f:
                lines = f.readlines()
            
            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) != 5:
                    print(f"Warning: Invalid label format in {label_path}. Skipping.")
                    continue
                class_id = int(parts[0])
                new_class_id = master_map[dataset_name].get(class_id, -1)
                if new_class_id == -1:
                    print(f"Warning: Class ID {class_id} not in master_map for {img_filename}. Skipping.")
                    continue
                new_lines.append(f"{new_class_id} {' '.join(parts[1:])}\n")
            
            if not new_lines:
                continue
            
            new_img_path = os.path.join(output_dir, 'images', target_split, f"{dataset_name}_{img_filename}")
            new_label_path = os.path.join(output_dir, 'labels', target_split, f"{dataset_name}_{img_filename.replace('.png', '.txt').replace('.jpg', '.txt')}")
            
            shutil.copy(img_path, new_img_path)
            with open(new_label_path, 'w') as f:
                f.writelines(new_lines)
            processed_count += 1

print(f"Processed {processed_count} images from VNTS, Chinese, and Indian datasets.")