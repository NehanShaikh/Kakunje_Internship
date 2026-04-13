import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.svm import SVC 
from sklearn.tree import DecisionTreeClassifier 
import joblib 
 
df=pd.read_csv("weather.csv") 
df=df.drop(columns=["date"]) 
 
x=df.drop(columns=["weather"]) 
y=df["weather"] 
 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42) 
 
models={ 
    "KNN":KNeighborsClassifier(), 
    "SVM":SVC(), 
    "Decision Tree":DecisionTreeClassifier() 
} 
 
best_model=None 
best_accuracy=0 
best_name="" 
 
print("Model Accuracy") 
 
for name, model in models.items(): 
    model.fit(x_train,y_train) 
    y_pred=model.predict(x_test) 
    accuracy=accuracy_score(y_test,y_pred) 
 
    print(f"{name}: {accuracy*100}%") 
 
    if accuracy > best_accuracy: 
        best_accuracy=accuracy 
        best_model=model 
        best_name=name 
 
print(f"Best Model: {best_name} ({best_accuracy*100}%)") 
 
joblib.dump(best_model,"weather_model.pkl") 
print("Model saved as weather_model.pkl")
