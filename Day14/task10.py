# Multiple Color Buttons
import tkinter as tk

root = tk.Tk()

def change_color(color):
    root.configure(bg=color)

tk.Button(root, text="Red",
          command=lambda: change_color("red")).pack(pady=5)

tk.Button(root, text="Green",
          command=lambda: change_color("green")).pack(pady=5)

tk.Button(root, text="Blue",
          command=lambda: change_color("blue")).pack(pady=5)

root.mainloop()
