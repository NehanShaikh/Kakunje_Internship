# Task9
import tkinter as tk

def calculate(op):
    n1 = float(e1.get())
    n2 = float(e2.get())

    if op == "add":
        result = n1 + n2
    elif op == "sub":
        result = n1 - n2
    elif op == "mul":
        result = n1 * n2
    else:
        result = n1 / n2

    lbl.config(text="Result: " + str(result))

root = tk.Tk()

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.pack()
e2.pack()

tk.Button(root, text="Add", command=lambda: calculate("add")).pack()
tk.Button(root, text="Subtract", command=lambda: calculate("sub")).pack()
tk.Button(root, text="Multiply", command=lambda: calculate("mul")).pack()
tk.Button(root, text="Divide", command=lambda: calculate("div")).pack()

lbl = tk.Label(root)
lbl.pack()

root.mainloop()
