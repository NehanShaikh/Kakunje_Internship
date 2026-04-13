# ============================
# Task - Diabetes Prediction GUI
# ============================

import tkinter as tk
import joblib

# Load model
try:
    model = joblib.load("diabetes_model.pkl")
except:
    print("Run dtrain.py first")
    exit()

# Prediction function
def predict():
    try:
        values = [
            float(entry1.get()),  # Pregnancies
            float(entry2.get()),  # Glucose
            float(entry3.get()),  # BloodPressure
            float(entry4.get()),  # SkinThickness
            float(entry5.get()),  # Insulin
            float(entry6.get()),  # BMI
            float(entry7.get()),  # DiabetesPedigreeFunction
            float(entry8.get())   # Age
        ]

        prediction = model.predict([values])[0]

        if prediction == 1:
            result.config(text="Diabetic")
        else:
            result.config(text="Not Diabetic")

    except:
        result.config(text="Enter valid values!")

# GUI
root = tk.Tk()
root.title("Diabetes Prediction App")
root.geometry("400x500")

tk.Label(root, text="Enter Patient Details", font=("Arial", 14)).pack(pady=10)

labels = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DPF", "Age"
]

entries = []

for label in labels:
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8 = entries

tk.Button(root, text="Predict", command=predict).pack(pady=15)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack()

root.mainloop()
