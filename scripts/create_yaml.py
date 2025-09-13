import yaml
from master_map import unified_classes

data = {
    'train': r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\GSTRB\merged_dataset\images\train',
    'val': r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\GSTRB\merged_dataset\images\val',
    'test': r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\GSTRB\merged_dataset\images\test',
    'nc': len(unified_classes),
    'names': unified_classes
}

with open(r'C:\Users\kienb\OneDrive\Desktop\DNCNTT\GSTRB\merged_dataset\data.yaml', 'w') as f:
    yaml.dump(data, f)

print("Created data.yaml")

