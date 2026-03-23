import os
import numpy as np
from PIL import Image
from skimage.feature import hog
from skimage.color import rgb2gray
from skimage.transform import resize
 
IMG_SIZE = (128, 128)
 
LABEL_MAP = {
    "cardboard": "Recyclable",
    "glass":     "Recyclable",
    "metal":     "Recyclable",
    "paper":     "Recyclable",
    "plastic":   "Recyclable",
    "trash":     "Hazardous",
    "general":   "Hazardous",
    "organic":   "Organic",
    "biological": "Organic",
    "e-waste":   "Hazardous",
    "medical":   "Hazardous",
}
def load_image(path):
    img = Image.open(path).convert("RGB")
    img = img.resize(IMG_SIZE)
    return np.array(img)
 
def extract_features(img_array):
    gray = rgb2gray(img_array)
    features = hog(
        gray,
        orientations=8,
        pixels_per_cell=(16, 16),
        cells_per_block=(2, 2),
        feature_vector=True
    )
    return features
 
def load_dataset(data_dir):
    X = []
    y = []
 
    for class_folder in os.listdir(data_dir):
        class_path = os.path.join(data_dir, class_folder)
        if not os.path.isdir(class_path):
            continue
 
        label = LABEL_MAP.get(class_folder.lower(), "Hazardous")
        print(f"Loading class: {class_folder} → {label}")
 
        for img_file in os.listdir(class_path):
            if not img_file.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            img_path = os.path.join(class_path, img_file)
            try:
                img = load_image(img_path)
                features = extract_features(img)
                X.append(features)
                y.append(label)
            except Exception as e:
                print(f"Skipping {img_file}: {e}")
 
    return np.array(X), np.array(y)