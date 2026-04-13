import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

# Task 1
window1 = QWidget()
window1.setWindowTitle("Task 1")
layout1 = QVBoxLayout()
label1 = QLabel("Hello Nehan")
label1.setAlignment(Qt.AlignCenter)
label1.setStyleSheet("font-size:20px;")
layout1.addWidget(label1)
window1.setLayout(layout1)
window1.show()

# Task 2
window2 = QWidget()
window2.setWindowTitle("Task 2")
layout2 = QVBoxLayout()

label2 = QLabel("")
button2 = QPushButton("Click Me")

def show_message():
    label2.setText("Button Clicked")

button2.clicked.connect(show_message)

layout2.addWidget(button2)
layout2.addWidget(label2)
window2.setLayout(layout2)
window2.show()

# Task 3
window3 = QWidget()
window3.setWindowTitle("Task 3")
layout3 = QVBoxLayout()

entry1 = QLineEdit()
entry2 = QLineEdit()
result3 = QLabel("")
button3 = QPushButton("Add")

def add_numbers():
    num1 = int(entry1.text())
    num2 = int(entry2.text())
    result3.setText("Sum = " + str(num1 + num2))

button3.clicked.connect(add_numbers)

layout3.addWidget(entry1)
layout3.addWidget(entry2)
layout3.addWidget(button3)
layout3.addWidget(result3)

window3.setLayout(layout3)
window3.show()

# Task 4
window4 = QWidget()
window4.setWindowTitle("Task 4")
layout4 = QVBoxLayout()

button4 = QPushButton("Change Color")

def change_color():
    colors = ["red","green","blue","yellow","orange","pink"]
    window4.setStyleSheet("background-color:" + random.choice(colors))

button4.clicked.connect(change_color)

layout4.addWidget(button4)
window4.setLayout(layout4)
window4.show()

# Task 5
window5 = QWidget()
window5.setWindowTitle("Task 5")
layout5 = QVBoxLayout()

label5 = QLabel("0")
button5 = QPushButton("Increase")

count = 0
def increase():
    global count
    count += 1
    label5.setText(str(count))

button5.clicked.connect(increase)

layout5.addWidget(label5)
layout5.addWidget(button5)
window5.setLayout(layout5)
window5.show()

# Task 6
window6 = QWidget()
window6.setWindowTitle("Task 6")
layout6 = QVBoxLayout()

combo = QComboBox()
combo.addItems(["Python","Java","C","C++","JavaScript"])

label6 = QLabel("")

def show_language():
    label6.setText("Selected: " + combo.currentText())

combo.currentIndexChanged.connect(show_language)

layout6.addWidget(combo)
layout6.addWidget(label6)
window6.setLayout(layout6)
window6.show()

# Task 7
window7 = QWidget()
window7.setWindowTitle("Task 7")
layout7 = QVBoxLayout()

name_entry = QLineEdit()
age_entry = QLineEdit()
course_entry = QLineEdit()

button7 = QPushButton("Submit")
result7 = QLabel("")

def submit():
    name = name_entry.text()
    result7.setText("Registered: " + name)

button7.clicked.connect(submit)

layout7.addWidget(name_entry)
layout7.addWidget(age_entry)
layout7.addWidget(course_entry)
layout7.addWidget(button7)
layout7.addWidget(result7)

window7.setLayout(layout7)
window7.show()

sys.exit(app.exec_())
