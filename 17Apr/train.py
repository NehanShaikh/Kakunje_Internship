# train.py

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import json

IMAGE_SIZE = (224, 224)
batch_size = 32

train_path = "C:\\Users\\HP\\Downloads\\Cards Image dataset\\Cards Image dataset\\train"
test_path = "C:\\Users\\HP\\Downloads\\Cards Image dataset\\Cards Image dataset\\test"

datagen = ImageDataGenerator(rescale=1./255)

train_ds = datagen.flow_from_directory(
    train_path,
    target_size=IMAGE_SIZE,
    batch_size=batch_size,
    class_mode='categorical'
)

val_ds = datagen.flow_from_directory(
    test_path,
    target_size=IMAGE_SIZE,
    batch_size=batch_size,
    class_mode='categorical'
)

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dense(train_ds.num_classes, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(train_ds, epochs=10, validation_data=val_ds)

model.save("cards_model.h5")
print("Model saved successfully")

with open("labels.json", "w") as f:
    json.dump(train_ds.class_indices, f)

print("Labels saved successfully")
