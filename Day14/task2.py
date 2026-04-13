# Simple Label
import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Welcome to Tkinter",
                 fg="white", bg="blue")
label.pack(pady=20)

root.mainloop()
