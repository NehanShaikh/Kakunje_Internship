# ============================
# Task - Diabetes Prediction Training
# ============================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("diabetes.csv")

# Features and Target
X = df.drop(columns=["Outcome"])
y = df["Outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier()
}

best_model = None
best_accuracy = 0
best_name = ""

print("Model Accuracy:\n")

# Train and compare
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"{name}: {acc * 100:.2f}%")

    if acc >= best_accuracy:
        best_model = model
        best_accuracy = acc
        best_name = name

print(f"\nBest Model: {best_name} ({best_accuracy * 100:.2f}%)")

# Save model
joblib.dump(best_model, "diabetes_model.pkl")
print("Model saved as diabetes_model.pkl")
