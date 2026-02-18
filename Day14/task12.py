# Radio Button Selection
import tkinter as tk

root = tk.Tk()

gender = tk.StringVar()

tk.Radiobutton(root, text="Male",
               variable=gender, value="Male").pack()
tk.Radiobutton(root, text="Female",
               variable=gender, value="Female").pack()

label = tk.Label(root)
label.pack()

def show_selection():
    label.config(text="Selected: " + gender.get())

tk.Button(root, text="Submit",
          command=show_selection).pack()

root.mainloop()
