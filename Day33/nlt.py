# NLTK TASKS
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer

# Task 1
text="Natural Language Processing with Python"
print(word_tokenize(text))

# Task 2
para="NLP is interesting. It helps computers understand language."
print(sent_tokenize(para))

# Task 3
words=word_tokenize("This is a simple sentence for stop word removal")
filtered=[w for w in words if w.lower() not in stopwords.words('english')]
print(filtered)

# Task 4
ps=PorterStemmer()
print(ps.stem("running"))

# Task 5
lem=WordNetLemmatizer()
print(lem.lemmatize("running",pos="v"))

# Task 6
tokens=word_tokenize("Python is a powerful programming language")
print(nltk.pos_tag(tokens))
