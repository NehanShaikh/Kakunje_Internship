from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

data = pd.read_csv("D:\\Internship\\Day39\\Iris.csv")

data['Species'] = data['Species'].map({
    'Iris-setosa': 0,
    'Iris-versicolor': 1,
    'Iris-virginica': 2
})

x = data.drop(['Species','Id'], axis=1)
y = data['Species']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

model = LogisticRegression(max_iter=200)
model.fit(x_train, y_train)

result = model.predict(pd.DataFrame([[5.1,3.5,1.4,0.2]], columns=x.columns))
print("Predicted Class:", result)
