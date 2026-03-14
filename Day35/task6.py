import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_water():
    d1 = float(day1.get())
    d2 = float(day2.get())
    d3 = float(day3.get())

    data = {
        "Day":["Mon","Tue","Wed"],
        "Water":[d1,d2,d3]
    }

    df = pd.DataFrame(data)

    avg = np.mean(df["Water"])

    result.config(text=f"Average Water Intake: {avg} Liters")

    plt.plot(df["Day"],df["Water"],marker="o")
    plt.title("Water Intake Tracker")
    plt.xlabel("Days")
    plt.ylabel("Liters")
    plt.show()

root = tk.Tk()
root.title("Water Intake Tracker")

tk.Label(root,text="Monday Intake (L)").pack()
day1 = tk.Entry(root)
day1.pack()

tk.Label(root,text="Tuesday Intake (L)").pack()
day2 = tk.Entry(root)
day2.pack()

tk.Label(root,text="Wednesday Intake (L)").pack()
day3 = tk.Entry(root)
day3.pack()

tk.Button(root,text="Analyze Water Intake",command=analyze_water).pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()
