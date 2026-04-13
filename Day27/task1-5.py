# Task 1 – Random Password Generator (Tkinter)
import tkinter as tk
import random
import string

def generate_password():
    length = int(entry_length.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    result_label.config(text=password)

root = tk.Tk()
root.title("Random Password Generator")

tk.Label(root, text="Enter Password Length").pack()

entry_length = tk.Entry(root)
entry_length.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

# Task 2 – Multiplication Table Generator (Tkinter)
import tkinter as tk

def generate_table():
    number = int(entry_num.get())
    output = ""
    for i in range(1, 11):
        output += f"{number} x {i} = {number*i}\n"
    result_label.config(text=output)

root = tk.Tk()
root.title("Multiplication Table Generator")

tk.Label(root, text="Enter Number").pack()

entry_num = tk.Entry(root)
entry_num.pack()

tk.Button(root, text="Generate Table", command=generate_table).pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()

# Task 3 – Dice Rolling Simulator (Tkinter)
import tkinter as tk
import random

def roll_dice():
    number = random.randint(1,6)
    result_label.config(text=f"Dice Result: {number}")

root = tk.Tk()
root.title("Dice Rolling Simulator")

tk.Button(root, text="Roll Dice", command=roll_dice).pack()

result_label = tk.Label(root, text="Click button to roll dice")
result_label.pack()

root.mainloop()

# Task 4 – Random Number Guessing Game (Tkinter)
import tkinter as tk
import random

target = random.randint(1,10)

def check_guess():
    guess = int(entry_guess.get())

    if guess == target:
        result_label.config(text="Correct Guess!")
    else:
        result_label.config(text="Wrong Guess!")

root = tk.Tk()
root.title("Number Guessing Game")

tk.Label(root, text="Guess number between 1-10").pack()

entry_guess = tk.Entry(root)
entry_guess.pack()

tk.Button(root, text="Check Guess", command=check_guess).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

# Task 5 – Word Counter (Tkinter)
import tkinter as tk

def count_words():
    text = text_box.get("1.0", tk.END)

    words = len(text.split())
    characters = len(text) - 1

    result_label.config(text=f"Words: {words}  Characters: {characters}")

root = tk.Tk()
root.title("Word Counter")

text_box = tk.Text(root, height=5, width=40)
text_box.pack()

tk.Button(root, text="Count Words", command=count_words).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
