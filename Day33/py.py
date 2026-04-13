# PYQT TASKS
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QLineEdit

app=QApplication(sys.argv)

# Task 1
win=QWidget()
win.setWindowTitle("Basic Window")
layout=QVBoxLayout()
layout.addWidget(QLabel("Hello PyQt"))
win.setLayout(layout)
win.show()

# Task 2
win2=QWidget()
layout2=QVBoxLayout()
label=QLabel("")
btn=QPushButton("Click")

def show():
    label.setText("Button Clicked")

btn.clicked.connect(show)
layout2.addWidget(btn)
layout2.addWidget(label)
win2.setLayout(layout2)
win2.show()

# Task 3
win3=QWidget()
layout3=QVBoxLayout()
u=QLineEdit()
p=QLineEdit()
p.setEchoMode(QLineEdit.Password)
layout3.addWidget(u)
layout3.addWidget(p)
layout3.addWidget(QPushButton("Login"))
win3.setLayout(layout3)
win3.show()

sys.exit(app.exec_())
