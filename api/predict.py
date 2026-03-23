import sys
import numpy as np
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

sys.path.append(r"C:\Users\Admin\Desktop\waste classifier\model")

MODEL_PATH = r"C:\Users\Admin\Desktop\waste classifier\model\model_cnn.h5"
CLASS_INDEX_PATH = r"C:\Users\Admin\Desktop\waste classifier\model\class_indices.pkl"

IMG_SIZE = (224, 224)

DISPOSAL_TIPS = {
    "Recyclable": "Clean the item and place it in the blue recycling bin.",
    "Organic":    "Place in the green compost bin or home compost heap.",
    "Hazardous":  "Do NOT throw in regular bins. Take to a hazardous waste facility.",
}

CLASS_TO_LABEL = {
    "general":  "Hazardous",
    "glass":    "Recyclable",
    "organic":  "Organic",
    "paper":    "Recyclable",
    "plastic":  "Recyclable",
}

model = load_model(MODEL_PATH)
class_indices = joblib.load(CLASS_INDEX_PATH)
index_to_class = {v: k for k, v in class_indices.items()}

def predict_image(image_path: str) -> dict:
    img = image.load_img(image_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    confidence = round(float(np.max(predictions[0])) * 100, 2)

    raw_class = index_to_class[predicted_index]
    category = CLASS_TO_LABEL.get(raw_class, "Hazardous")
    tip = DISPOSAL_TIPS.get(category, "Dispose responsibly.")

    return {
        "category":     category,
        "confidence":   confidence,
        "disposal_tip": tip,
        "raw_class":    raw_class,
    }