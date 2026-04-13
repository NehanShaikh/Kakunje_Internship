import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_steps():
    d1 = int(day1.get())
    d2 = int(day2.get())
    d3 = int(day3.get())

    data = {
        "Day":["Mon","Tue","Wed"],
        "Steps":[d1,d2,d3]
    }

    df = pd.DataFrame(data)

    avg = np.mean(df["Steps"])

    result.config(text=f"Average Steps: {avg}")

    plt.plot(df["Day"],df["Steps"],marker="o")
    plt.title("Fitness Progress")
    plt.xlabel("Days")
    plt.ylabel("Steps")
    plt.show()

root = tk.Tk()
root.title("Fitness Activity Tracker")

tk.Label(root,text="Monday Steps").pack()
day1 = tk.Entry(root)
day1.pack()

tk.Label(root,text="Tuesday Steps").pack()
day2 = tk.Entry(root)
day2.pack()

tk.Label(root,text="Wednesday Steps").pack()
day3 = tk.Entry(root)
day3.pack()

tk.Button(root,text="Analyze Activity",command=analyze_steps).pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()
