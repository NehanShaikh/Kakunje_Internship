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
