# Message Box
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

tk.Button(root, text="Info",
          command=lambda: messagebox.showinfo("Info", "This is info message")).pack()

tk.Button(root, text="Warning",
          command=lambda: messagebox.showwarning("Warning", "This is warning")).pack()

tk.Button(root, text="Error",
          command=lambda: messagebox.showerror("Error", "This is error")).pack()

root.mainloop()
