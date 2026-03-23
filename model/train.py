import os
import numpy as np
import joblib
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

DATA_DIR = r"C:\Users\Admin\Desktop\waste classifier\model\final_dataset\train"
MODEL_PATH = "model_cnn.h5"
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 20

CLASS_MAP = {
    "general":  "Hazardous",
    "glass":    "Recyclable",
    "organic":  "Organic",
    "paper":    "Recyclable",
    "plastic":  "Recyclable",
}

def train():
    print("Setting up data generators...")

    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.2
    )

    train_generator = train_datagen.flow_from_directory(
        DATA_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )

    val_generator = train_datagen.flow_from_directory(
        DATA_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )

    print(f"Classes found: {train_generator.class_indices}")

    print("Building MobileNetV2 model...")
    base_model = MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights='imagenet'
    )
    base_model.trainable = False

    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dropout(0.3),
        Dense(128, activation='relu'),
        Dropout(0.2),
        Dense(train_generator.num_classes, activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    callbacks = [
        EarlyStopping(patience=5, restore_best_weights=True),
        ModelCheckpoint(MODEL_PATH, save_best_only=True)
    ]

    print("Training model... please wait!")
    model.fit(
        train_generator,
        epochs=EPOCHS,
        validation_data=val_generator,
        callbacks=callbacks
    )

    loss, acc = model.evaluate(val_generator)
    print(f"\nFinal Accuracy: {acc * 100:.2f}%")
    print(f"Model saved to {MODEL_PATH}")

    joblib.dump(train_generator.class_indices, "class_indices.pkl")
    print("Class indices saved!")

if __name__ == "__main__":
    train()