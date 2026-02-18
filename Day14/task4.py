# Multiple Labels
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Label 1", fg="red").pack(pady=5)
tk.Label(root, text="Label 2", fg="green").pack(pady=5)
tk.Label(root, text="Label 3", fg="blue").pack(pady=5)

root.mainloop()
