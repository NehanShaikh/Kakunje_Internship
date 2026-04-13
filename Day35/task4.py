import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_attendance():
    total = int(total_classes.get())
    attended = int(attended_classes.get())

    percentage = (attended/total)*100

    result.config(text=f"Attendance Percentage: {percentage:.2f}%")

    labels = ["Attended","Missed"]
    values = [attended,total-attended]

    plt.pie(values,labels=labels,autopct='%1.1f%%')
    plt.title("Attendance Distribution")
    plt.show()

root = tk.Tk()
root.title("Attendance Analyzer")

tk.Label(root,text="Total Classes").pack()
total_classes = tk.Entry(root)
total_classes.pack()

tk.Label(root,text="Classes Attended").pack()
attended_classes = tk.Entry(root)
attended_classes.pack()

tk.Button(root,text="Analyze Attendance",command=analyze_attendance).pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()
