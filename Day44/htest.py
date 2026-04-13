import tkinter as tk
import joblib
import pandas as pd

try:
    model = joblib.load("housing_model.pkl")
except:
    print("Please run htrain.py first")
    exit()

def predict():
    try:
        values = [
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get()),
            float(entry5.get())
        ]

        df = pd.read_csv("housing.csv")
        df = df.dropna()
        df = pd.get_dummies(df, drop_first=True)

        columns = df.drop(columns=["price"]).columns
        data = pd.DataFrame([[0]*len(columns)], columns=columns)

        base_cols = ["area","bedrooms","bathrooms","stories","parking"]
        for i, col in enumerate(base_cols):
            data[col] = values[i]

        prediction = model.predict(data)[0]

        result.config(text=f"Predicted Price: {prediction:.2f}")

    except Exception as e:
        result.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("Housing Prediction App")
root.geometry("350x450")

tk.Label(root, text="Enter Housing Details", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Area").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Bedrooms").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Bathrooms").pack()
entry3 = tk.Entry(root)
entry3.pack()

tk.Label(root, text="Stories").pack()
entry4 = tk.Entry(root)
entry4.pack()

tk.Label(root, text="Parking").pack()
entry5 = tk.Entry(root)
entry5.pack()

tk.Button(root, text="Predict", command=predict).pack(pady=15)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack()

root.mainloop()
