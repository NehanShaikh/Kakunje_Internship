import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_expense():
    food_amt = float(food.get())
    travel_amt = float(travel.get())
    shopping_amt = float(shopping.get())
    other_amt = float(other.get())

    data = {
        "Category":["Food","Travel","Shopping","Other"],
        "Amount":[food_amt,travel_amt,shopping_amt,other_amt]
    }

    df = pd.DataFrame(data)

    total = np.sum(df["Amount"])
    average = np.mean(df["Amount"])

    result.config(text=f"Total Expense: {total}\nAverage Expense: {average}")

    plt.pie(df["Amount"],labels=df["Category"],autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()


root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("500x500")

tk.Label(root,text="Food Expense").pack()
food = tk.Entry(root)
food.pack()

tk.Label(root,text="Travel Expense").pack()
travel = tk.Entry(root)
travel.pack()

tk.Label(root,text="Shopping Expense").pack()
shopping = tk.Entry(root)
shopping.pack()

tk.Label(root,text="Other Expense").pack()
other = tk.Entry(root)
other.pack()

tk.Button(root,text="Analyze Expense",command=analyze_expense).pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()
