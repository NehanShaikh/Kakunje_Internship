import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_units():
    jan = int(january.get())
    feb = int(february.get())
    mar = int(march.get())

    data = {
        "Month":["Jan","Feb","Mar"],
        "Units":[jan,feb,mar]
    }

    df = pd.DataFrame(data)

    total = np.sum(df["Units"])
    avg = np.mean(df["Units"])

    result.config(text=f"Total Units: {total}\nAverage Units: {avg}")

    plt.plot(df["Month"],df["Units"],marker="o")
    plt.title("Electricity Usage")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.show()

root = tk.Tk()
root.title("Electricity Bill Analyzer")

tk.Label(root,text="January Units").pack()
january = tk.Entry(root)
january.pack()

tk.Label(root,text="February Units").pack()
february = tk.Entry(root)
february.pack()

tk.Label(root,text="March Units").pack()
march = tk.Entry(root)
march.pack()

tk.Button(root,text="Analyze Usage",command=analyze_units).pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()
