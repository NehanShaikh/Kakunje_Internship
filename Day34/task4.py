import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_quiz():
    s1 = int(student1.get())
    s2 = int(student2.get())
    s3 = int(student3.get())
    s4 = int(student4.get())

    data = {
        "Student":["A","B","C","D"],
        "Score":[s1,s2,s3,s4]
    }

    df = pd.DataFrame(data)

    average = np.mean(df["Score"])
    highest = np.max(df["Score"])

    result.config(text=f"Average Score: {average}\nHighest Score: {highest}")

    plt.bar(df["Student"],df["Score"])
    plt.title("Quiz Results")
    plt.xlabel("Students")
    plt.ylabel("Score")
    plt.show()


root = tk.Tk()
root.title("Quiz Result Analyzer")
root.geometry("500x500")

tk.Label(root,text="Student A Score").pack()
student1 = tk.Entry(root)
student1.pack()

tk.Label(root,text="Student B Score").pack()
student2 = tk.Entry(root)
student2.pack()

tk.Label(root,text="Student C Score").pack()
student3 = tk.Entry(root)
student3.pack()

tk.Label(root,text="Student D Score").pack()
student4 = tk.Entry(root)
student4.pack()

tk.Button(root,text="Analyze Quiz",command=analyze_quiz).pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()
