# Task1
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

def show_message():
    msg = QMessageBox()
    msg.setWindowTitle("Message")
    msg.setText("Hello Student!")
    msg.exec_()

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Simple PyQt Window")
window.setGeometry(100, 100, 300, 200)

button = QPushButton("Click Me", window)
button.move(100, 80)

button.clicked.connect(show_message)

window.show()


# Task2
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

text = "Online shopping has become very convenient today. Customers expect fast delivery and good product quality."

sentences = sent_tokenize(text)
print("\nSentence Tokens:")
print(sentences)

words = word_tokenize(text)
print("\nWord Tokens:")
print(words)

stemmer = PorterStemmer()

words_list = ["delivery", "delivering", "delivered", "customers", "shopping", "quality"]

stemmed_words = [stemmer.stem(word) for word in words_list]

print("\nOriginal Words:")
print(words_list)

print("\nStemmed Words:")
print(stemmed_words)

tokens = word_tokenize("Online shopping has become very convenient today.")
pos_tags = pos_tag(tokens)

print("\nPOS Tagged Words:")
print(pos_tags)

stop_words = set(stopwords.words("english"))
tokens = word_tokenize("Online shopping has become very convenient today.")
filtered_words = [word for word in tokens if word.lower() not in stop_words]

print("\nOriginal Words:")
print(tokens)

print("\nFiltered Words (Stopwords Removed):")
print(filtered_words)


sys.exit(app.exec_())
