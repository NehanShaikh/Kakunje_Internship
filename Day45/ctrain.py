import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score 
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.svm import SVR 
from sklearn.tree import DecisionTreeRegressor 
from sklearn.preprocessing import LabelEncoder 
import joblib 
 
df=pd.read_csv("car_price.csv") 
 
encoders={} 
cols=["Brand","Model","Fuel_Type","Transmission"] 
 
for col in cols: 
    le=LabelEncoder() 
    df[col]=le.fit_transform(df[col]) 
    encoders[col]=le 
print(df.head()) 
 
x=df.drop(columns=["Price"]) 
y=df["Price"] 
 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42) 
 
models={"KNN":KNeighborsRegressor(), 
        "SVR":SVR(), 
        "Decision Tree":DecisionTreeRegressor() 
        } 
 
best_model=None 
best_score=0 
best_name="" 
 
print("Model Performance") 
 
for name,model in models.items(): 
    model.fit(x_train,y_train) 
    y_pred=model.predict(x_test) 
    score=r2_score(y_test,y_pred) 
     
    print(f"{name}:{score}") 
     
    if score>best_score: 
        best_score=score 
        best_model=model 
        best_name=name 
 
print(f"Best Model:{best_name}({best_score})") 
 
joblib.dump(best_model,"car_model.pkl") 
joblib.dump(encoders,"encoders.pkl") 
 
print("Model saved")
