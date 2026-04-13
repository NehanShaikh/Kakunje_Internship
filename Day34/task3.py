import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_books():
    book1_copies = int(book1.get())
    book2_copies = int(book2.get())
    book3_copies = int(book3.get())

    data = {
        "Book":["Python","Java","C++"],
        "Copies":[book1_copies,book2_copies,book3_copies]
    }

    df = pd.DataFrame(data)

    total = np.sum(df["Copies"])
    average = np.mean(df["Copies"])

    result.config(text=f"Total Books: {total}\nAverage Copies: {average}")

    plt.bar(df["Book"],df["Copies"])
    plt.title("Library Book Distribution")
    plt.xlabel("Books")
    plt.ylabel("Copies")
    plt.show()


root = tk.Tk()
root.title("Library Book Data Analyzer")
root.geometry("500x500")

tk.Label(root,text="Python Book Copies").pack()
book1 = tk.Entry(root)
book1.pack()

tk.Label(root,text="Java Book Copies").pack()
book2 = tk.Entry(root)
book2.pack()

tk.Label(root,text="C++ Book Copies").pack()
book3 = tk.Entry(root)
book3.pack()

tk.Button(root,text="Analyze Books",command=analyze_books).pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()
