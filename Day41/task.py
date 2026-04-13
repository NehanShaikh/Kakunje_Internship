# Decision Tree for Spam Detection: 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.feature_extraction.text import CountVectorizer 
df=pd.read_csv("email.csv") 
x=df["Message"] 
y=df["Category"] 
le=LabelEncoder() 
y=le.fit_transform(y) 
cv = CountVectorizer()             
x = cv.fit_transform(x) 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) 
model=DecisionTreeClassifier(criterion="gini",max_depth=3) 
model.fit(x_train,y_train) 
y_pred=model.predict(x_test) 
print(y_pred) 


# Random Forest for Spam Detection: 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.feature_extraction.text import CountVectorizer 
df=pd.read_csv("email.csv")

x=df["Message"] 
y=df["Category"]
 
le=LabelEncoder() 
y=le.fit_transform(y) 
 
cv = CountVectorizer()             
x = cv.fit_transform(x) 
 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) 
 
model=RandomForestClassifier(criterion="gini",n_estimators=10) 
model.fit(x_train,y_train) 
 
y_pred=model.predict(x_test) 
print(y_pred)
