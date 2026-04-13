# ANN
import numpy as np 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
import tensorflow as tf 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense 
 
data=load_iris() 
x=data.data 
y=data.target 
 
x_train, x_test, y_train, y_test = train_test_split (x, y, test_size =0.2,random_state=42) 
 
sc = StandardScaler () 
x_train = sc.fit_transform(x_train) 
x_test = sc.transform(x_test) 
 
model = Sequential () 
model.add (Dense (8, activation='relu',input_dim=4)) 
model.add(Dense(6,activation='relu')) 
model.add(Dense(3,activation='softmax')) 
 
model.compile(optimizer="adam", 
              loss="sparse_categorical_crossentropy", 
              metrics=["accuracy"]) 
 
model.fit(x_train,y_train,epochs=100) 
loss,accuracy=model.evaluate(x_test,y_test) 
 
print("Accuracy: ",accuracy) 
 
sample=np.array([[5.1,3.5,1.4,0.2]]) 
sample=sc.transform(sample) 
prediction=model.predict(sample) 
print("Predicted class: ",np.argmax(prediction)) 

# CNN 
import tensorflow as tf 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense,Conv2D,MaxPooling2D,Flatten 
 
(x_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data(path="mnist.npz") 
 
x_train=x_train/255.0 
x_test=x_test/255.0 
 
x_train=x_train.reshape(-1,28,28,1) 
x_test=x_test.reshape(-1,28,28,1) 
 
model=Sequential() 
model.add(Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1))) 
model.add(MaxPooling2D(pool_size=(2,2))) 
model.add(Flatten()) 
model.add(Dense(128,activation='relu')) 
model.add(Dense(10,activation="softmax")) 
 
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy']) 
 
model.fit(x_train,y_train,epochs=2) 
 
model.save("mnist_cnn_model.keras") 
 
loss,accuracy=model.evaluate(x_test,y_test) 
print("Accuracy: ",accuracy) 
 
import numpy as np 
prediction=model.predict(x_test[:1]) 
 
print("Predicted digit: ",np.argmax(prediction))
