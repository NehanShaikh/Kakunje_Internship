# Confirmation Dialog
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def confirm_exit():
    result = messagebox.askyesno("Exit", "Do you want to exit?")
    if result:
        root.destroy()

tk.Button(root, text="Exit",
          command=confirm_exit).pack(pady=20)

root.mainloop()
