# Read Input
import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

label = tk.Label(root)
label.pack()

def show_input():
    name = entry.get()
    label.config(text="Hello " + name)

button = tk.Button(root, text="Submit",
                   command=show_input)
button.pack()

root.mainloop()
