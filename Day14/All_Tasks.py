# Create Window
import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter")
root.geometry("400x300")
root.configure(bg="lightblue")

root.mainloop()


# Simple Label
import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Welcome to Tkinter",
                 fg="white", bg="blue")
label.pack(pady=20)

root.mainloop()


# Font Formatting
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Nehan Shaikh",
                 font=("Arial", 20, "bold"))
label.pack(pady=20)

root.mainloop()


# Multiple Labels
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Label 1", fg="red").pack(pady=5)
tk.Label(root, text="Label 2", fg="green").pack(pady=5)
tk.Label(root, text="Label 3", fg="blue").pack(pady=5)

root.mainloop()


# Simple Button
import tkinter as tk

root = tk.Tk()

button = tk.Button(root, text="Submit",
                   bg="green", fg="white")
button.pack(pady=20)

root.mainloop()


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


# Entry Widget
import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root, bg="lightyellow", fg="blue")
entry.pack(pady=20)

root.mainloop()


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


# Grid Layout
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Age").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)

root.mainloop()


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


# Theme Change
import tkinter as tk

root = tk.Tk()

dark_mode = False

def toggle_theme():
    global dark_mode
    if dark_mode:
        root.configure(bg="white")
        button.config(text="Switch to Dark Mode")
        dark_mode = False
    else:
        root.configure(bg="black")
        button.config(text="Switch to Light Mode")
        dark_mode = True

button = tk.Button(root, text="Switch to Dark Mode",
                   command=toggle_theme)
button.pack(pady=50)

root.mainloop()
