# Naive bayes for wine dataset:
from sklearn.datasets import load_wine 
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import accuracy_score,confusion_matrix 
 
data=load_wine() 
 
x=data.data 
y=data.target 
 
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=42) 
 
model=GaussianNB() 
model.fit(x_train,y_train) 
 
y_pred=model.predict(x_test) 
print(y_pred) 
 
test=model.predict([x[0]]) 
print(test) 
 
acc=accuracy_score(y_test,y_pred) 
print(acc*100) 
 
print("Confusion Matrix") 
print(confusion_matrix(y_test,y_pred)) 
 
  
# SVM for wine dataset:
from sklearn.datasets import load_wine 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score, confusion_matrix 
 
data=load_wine() 
 
x=data.data 
y=data.target 
 
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=42) 
 
model=SVC(kernel="linear",C=1.0) 
model.fit(x_train,y_train) 
 
y_pred=model.predict(x_test) 
print(y_pred) 
 
test=model.predict([x[0]]) 
print(test) 
 
acc=accuracy_score(y_test,y_pred) 
print(acc*100) 
 
print("Confusion Matrix") 
print(confusion_matrix(y_test,y_pred))
