import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_score():
    p1 = int(player1.get())
    p2 = int(player2.get())
    p3 = int(player3.get())

    data = {
        "Player":["A","B","C"],
        "Score":[p1,p2,p3]
    }

    df = pd.DataFrame(data)

    avg = np.mean(df["Score"])

    result.config(text=f"Average Score: {avg}")

    plt.bar(df["Player"],df["Score"])
    plt.title("Cricket Score Comparison")
    plt.xlabel("Players")
    plt.ylabel("Score")
    plt.show()

root = tk.Tk()
root.title("Cricket Score Analyzer")

tk.Label(root,text="Player A Score").pack()
player1 = tk.Entry(root)
player1.pack()

tk.Label(root,text="Player B Score").pack()
player2 = tk.Entry(root)
player2.pack()

tk.Label(root,text="Player C Score").pack()
player3 = tk.Entry(root)
player3.pack()

tk.Button(root,text="Analyze Scores",command=analyze_score).pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()
