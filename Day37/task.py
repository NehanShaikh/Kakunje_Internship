import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("titanic.csv")

df = df[["PassengerId","Survived","Pclass","Age","SibSp","Parch","Fare"]]
df = df.fillna(0)

x = df.drop(columns=["Survived"])
y = df["Survived"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

acc = accuracy_score(y_test,y_pred)
print("Accuracy:",acc*100)

new_data = pd.DataFrame([[151,3,22,1,0,7.25]],
columns=["PassengerId","Pclass","Age","SibSp","Parch","Fare"])

y_p = knn.predict(new_data)
print("Prediction:",y_p)
