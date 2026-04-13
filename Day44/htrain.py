import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("housing.csv")
df = df.dropna()

df = pd.get_dummies(df, drop_first=True)
X = df.drop(columns=["price"])
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor()
}

best_model = None
best_score = 0
best_name = ""

print("Model Performance (R2 Score)")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    score = r2_score(y_test, y_pred)
    print(f"{name}: {score * 100:.2f}%")

    if score >= best_score:
        best_model = model
        best_score = score
        best_name = name

print(f"\nBest Model: {best_name} ({best_score * 100:.2f}%)")

joblib.dump(best_model, "housing_model.pkl")
print("Model saved as housing_model.pkl")
