import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def message () :
    msg.setText ("Hello")

app = QApplication (sys.argv)

window= QWidget ()
window.setWindowTitle ("My First PyQt Window")
window.resize (300,200)

label = QLabel("Hello from PyQt",window)
button = QPushButton ("Click Me", window)
msg = QLabel ("",window)

layout = QVBoxLayout ()

layout.addWidget (label)
layout.addWidget (button)
layout .addWidget (msg)

window. setLayout (layout)

button. clicked.connect (message)

window. show ()

sys.exit (app.exec_() )
