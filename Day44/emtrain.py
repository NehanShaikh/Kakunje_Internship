import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

import joblib
df = pd.read_csv("email.csv")

X = df["Message"]
y = df["Category"]

le = LabelEncoder()
y = le.fit_transform(y)

cv = CountVectorizer()
X = cv.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "Decision Tree": DecisionTreeClassifier()
}

best_model = None
best_accuracy = 0
best_name = ""

print("Model Accuracy:\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name}: {accuracy * 100:.2f}%")

    if accuracy > best_accuracy:
        best_model = model
        best_accuracy = accuracy
        best_name = name

print(f"\nBest Model: {best_name} ({best_accuracy * 100:.2f}%)")

joblib.dump(best_model, "best_model.pkl")
joblib.dump(cv, "vectorizer.pkl")
print("Model saved as best_model.pkl")
print("Vectorizer saved as vectorizer.pkl")
