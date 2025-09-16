import pandas as pd
import os
import shutil
import random
from master_map import master_map, unified_classes

# Paths
gtsrb_test_csv = r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\GSTRB\Test.csv'
gtsrb_image_dir = r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\GSTRB\Test'
output_dir = r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\GSTRB\merged_dataset'

# Create output folders
for split in ['train', 'val', 'test']:
    os.makedirs(os.path.join(output_dir, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels', split), exist_ok=True)

# Load CSV
test_df = pd.read_csv(gtsrb_test_csv)

# Split images (80% train, 10% val, 10% test)
random.seed(42)
image_files = list(test_df['Path'].apply(os.path.basename))
random.shuffle(image_files)
n_total = len(image_files)  # 12,630
n_train = int(0.8 * n_total)  # ~10,104
n_val = int(0.1 * n_total)    # ~1,263
train_files = image_files[:n_train]
val_files = image_files[n_train:n_train + n_val]
test_files = image_files[n_train + n_val:]

# Process images
processed_count = 0
missing_images = []
for idx, row in test_df.iterrows():
    img_filename = os.path.basename(row['Path'])
    img_path = os.path.join(gtsrb_image_dir, img_filename)
    
    if not os.path.exists(img_path):
        missing_images.append(img_filename)
        continue
    
    class_id = row['ClassId']
    new_class_id = master_map['gtsrb'].get(class_id, -1)
    if new_class_id == -1:
        print(f"Warning: Class ID {class_id} not in master_map. Skipping {img_filename}.")
        continue
    
    width, height = row['Width'], row['Height']
    x1, y1, x2, y2 = row['Roi.X1'], row['Roi.Y1'], row['Roi.X2'], row['Roi.Y2']
    
    x_center = ((x1 + x2) / 2) / width
    y_center = ((y1 + y2) / 2) / height
    bbox_width = (x2 - x1) / width
    bbox_height = (y2 - y1) / height
    
    split = 'train' if img_filename in train_files else 'val' if img_filename in val_files else 'test'
    new_img_path = os.path.join(output_dir, 'images', split, f"gtsrb_{img_filename}")
    label_path = os.path.join(output_dir, 'labels', split, f"gtsrb_{img_filename.replace('.png', '.txt')}")
    
    shutil.copy(img_path, new_img_path)
    with open(label_path, 'w') as f:
        f.write(f"{new_class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n")
    processed_count += 1

print(f"GTSRB converted to YOLO format. Processed {processed_count} images.")
if missing_images:
    print(f"Missing {len(missing_images)} images: {missing_images[:5]}")