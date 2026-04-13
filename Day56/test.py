import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import json
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model('vegetable_type_model.h5')

with open("D:\\Internship\\Day56\\Vegetable Images\\Vegetable Images\\labels.json", 'r') as f:
    class_indices = json.load(f)

labels = list(class_indices.keys())

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    result = model.predict(img)
    idx = np.argmax(result)

    return labels[idx]

def open_image():
    global img_path, panel

    img_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )

    img = Image.open(img_path)
    img = img.resize((300, 300))

    img_tk = ImageTk.PhotoImage(img)

    panel.config(image=img_tk)
    panel.image = img_tk

    result.config(text="")

def classify():
    if img_path:
        label = predict_image(img_path)
        result.config(text=f"Prediction: {label}")

root = tk.Tk()
root.title("Vegetable Type Prediction")
root.geometry('400x500')

panel = tk.Label(root)
panel.pack(pady=10)

btn_load = tk.Button(root, text="Load The Image", command=open_image)
btn_load.pack(pady=10)

btn_predict = tk.Button(root, text='Classify', command=classify)
btn_predict.pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 20))
result.pack(pady=20)

img_path = ""

root.mainloop()
