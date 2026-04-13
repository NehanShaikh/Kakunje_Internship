import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_salary():
    e1 = int(emp1.get())
    e2 = int(emp2.get())
    e3 = int(emp3.get())

    data = {
        "Employee":["A","B","C"],
        "Salary":[e1,e2,e3]
    }

    df = pd.DataFrame(data)

    avg = np.mean(df["Salary"])
    high = np.max(df["Salary"])
    low = np.min(df["Salary"])

    result.config(text=f"Average Salary: {avg}\nHighest Salary: {high}\nLowest Salary: {low}")

    plt.bar(df["Employee"],df["Salary"])
    plt.title("Employee Salary Distribution")
    plt.xlabel("Employees")
    plt.ylabel("Salary")
    plt.show()

root = tk.Tk()
root.title("Employee Salary Analyzer")

tk.Label(root,text="Employee A Salary").pack()
emp1 = tk.Entry(root)
emp1.pack()

tk.Label(root,text="Employee B Salary").pack()
emp2 = tk.Entry(root)
emp2.pack()

tk.Label(root,text="Employee C Salary").pack()
emp3 = tk.Entry(root)
emp3.pack()

tk.Button(root,text="Analyze Salary",command=analyze_salary).pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()
