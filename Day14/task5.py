# Simple Button
import tkinter as tk

root = tk.Tk()

button = tk.Button(root, text="Submit",
                   bg="green", fg="white")
button.pack(pady=20)

root.mainloop()
