import tkinter as tk
import joblib

try:
    model = joblib.load("best_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
except:
    print("Run training file first and save model + vectorizer")
    exit()

def predict():
    message = entry.get()

    if message == "":
        result.config(text="Please enter a message")
        return

    message_vector = vectorizer.transform([message])

    prediction = model.predict(message_vector)[0]

    if prediction == 1:
        output = "Spam"
    else:
        output = "Not Spam"

    result.config(text=f"Prediction: {output}")

root = tk.Tk()
root.title("Spam Detection App")
root.geometry("400x300")

tk.Label(root, text="Enter Email Message", font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

tk.Button(root, text="Predict", command=predict).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=10)

root.mainloop()
