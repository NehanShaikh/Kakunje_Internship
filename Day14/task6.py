# Button Action
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Click the button")
label.pack(pady=10)

def change_text():
    label.config(text="Button Clicked!", fg="red")

button = tk.Button(root, text="Click Me",
                   command=change_text)
button.pack()

root.mainloop()
