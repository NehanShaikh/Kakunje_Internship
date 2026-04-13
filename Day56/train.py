import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

IMAGE_SIZE = (224, 224)
Batch = 32

train_path = "D:\\Internship\\Day56\\Vegetable Images\\Vegetable Images\\train"

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_ds = datagen.flow_from_directory(
    train_path,
    target_size=IMAGE_SIZE,
    batch_size=Batch,
    class_mode="categorical",
    subset="training"
)

val_ds = datagen.flow_from_directory(
    train_path,
    target_size=IMAGE_SIZE,
    batch_size=Batch,
    class_mode="categorical",
    subset="validation"
)

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D(),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(train_ds.num_classes, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

model.fit(train_ds, epochs=10, validation_data=val_ds)

model.save('vegetable_type_model.h5')

print("The model is saved successfully")
