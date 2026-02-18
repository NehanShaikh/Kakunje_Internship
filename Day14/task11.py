# Mouse Click
import tkinter as tk

root = tk.Tk()

label = tk.Label(root)
label.pack()

def mouse_clicked(event):
    label.config(text="Mouse Clicked")

button = tk.Button(root, text="Click Me")
button.pack()

button.bind("<Button-1>", mouse_clicked)

root.mainloop()
