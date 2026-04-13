# TKINTER TASKS
import tkinter as tk

# Task 1
root = tk.Tk()
root.title("Basic Window")
root.geometry("300x200")
root.mainloop()

# Task 2
root = tk.Tk()
label = tk.Label(root,text="Hello")
label.pack()
btn = tk.Button(root,text="Click")
btn.pack()
root.mainloop()

# Task 3
def calc(op):
    a=int(e1.get())
    b=int(e2.get())
    if op=="add": r=a+b
    if op=="sub": r=a-b
    if op=="mul": r=a*b
    if op=="div": r=a/b
    result.config(text=str(r))

root=tk.Tk()
e1=tk.Entry(root)
e2=tk.Entry(root)
e1.pack()
e2.pack()
tk.Button(root,text="Add",command=lambda:calc("add")).pack()
tk.Button(root,text="Sub",command=lambda:calc("sub")).pack()
tk.Button(root,text="Mul",command=lambda:calc("mul")).pack()
tk.Button(root,text="Div",command=lambda:calc("div")).pack()
result=tk.Label(root,text="")
result.pack()
root.mainloop()

# Task 4
root=tk.Tk()
tk.Label(root,text="Username").pack()
tk.Entry(root).pack()
tk.Label(root,text="Password").pack()
tk.Entry(root,show="*").pack()
tk.Button(root,text="Login").pack()
root.mainloop()

# Task 5
def msg():
    label.config(text="Button Clicked")

root=tk.Tk()
btn=tk.Button(root,text="Click",command=msg)
btn.pack()
label=tk.Label(root,text="")
label.pack()
root.mainloop()

# Task 6
root=tk.Tk()
txt=tk.Entry(root)
txt.pack()
root.mainloop()

# Task 7
root=tk.Tk()
text=tk.Text(root)
text.pack()
root.mainloop()

# Task 8
root=tk.Tk()
menu=tk.Menu(root)
root.config(menu=menu)
filemenu=tk.Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
root.mainloop()
