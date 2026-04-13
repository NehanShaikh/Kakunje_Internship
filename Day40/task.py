import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
hours = [2, 3, 1]

df = pd.DataFrame({"Subject": subjects, "Hours": hours})

total = np.sum(df["Hours"])
avg = np.mean(df["Hours"])

print("Total Study Time:", total)
print("Average Study Time:", avg)

plt.bar(df["Subject"], df["Hours"])
plt.title("Study Time")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

food = ["Rice", "Milk", "Egg"]
calories = [200, 150, 100]

df = pd.DataFrame({"Food": food, "Calories": calories})

total = np.sum(df["Calories"])
print("Total Calories:", total)

plt.pie(df["Calories"], labels=df["Food"], autopct="%1.1f%%")
plt.title("Calorie Intake")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

products = ["Pen", "Book", "Bag"]
quantity = [50, 30, 20]

df = pd.DataFrame({"Product": products, "Quantity": quantity})

total = np.sum(df["Quantity"])
print("Total Stock:", total)

plt.bar(df["Product"], df["Quantity"])
plt.title("Stock Levels")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

numbers = [10, 20, 30, 40, 50]

df = pd.DataFrame({"Numbers": numbers})

print("Max:", np.max(df["Numbers"]))
print("Min:", np.min(df["Numbers"]))
print("Average:", np.mean(df["Numbers"]))

plt.plot(df["Numbers"])
plt.title("Number Comparison")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

players = ["A", "B", "C"]
scores = [80, 60, 90]

df = pd.DataFrame({"Player": players, "Score": scores})

print("Highest Score:", np.max(df["Score"]))

plt.bar(df["Player"], df["Score"])
plt.title("Game Scores")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hours = ["9AM", "10AM", "11AM", "12PM"]
vehicles = [50, 80, 120, 90]

df = pd.DataFrame({"Time": hours, "Vehicles": vehicles})

peak = df.iloc[np.argmax(df["Vehicles"])]
print("Peak Time:", peak["Time"])

plt.plot(df["Time"], df["Vehicles"])
plt.title("Traffic Analysis")
plt.show()

"""
Q7.  
TP = 50, FP = 5, FN = 10, TN = 35 
Total = 50 + 10 + 5 + 35 = 100 
Accuracy = (50 + 35) / 100 = 0.85 
Precision = 50 / (50 + 5) = 0.909 
Recall = 50 / (50 + 10) = 0.8333 
F1 Score = 2 × (0.909 × 0.8333) / (0.909 + 0.8333) 
F1 Score = 2 × 0.7574 / 1.7423 
F1 Score = 0.8694

Q8. 
Total = 40 + 5 + 5 + 10 + 30 + 10 + 5 + 5 + 40 = 150 
Accuracy = (40 + 30 + 40) / 150 = 0.7333 
Precision (A) = 40 / (40 + 10 + 5) = 0.7272 
Recall (A) = 40 / (40 + 5 + 5) = 0.8 
F1 Score (A) = 2 × (0.7272 × 0.8) / (0.7272 + 0.8) 
F1 Score (A) = 2 × 0.5817 / 1.5272 
F1 Score (A) = 0.7618 
Precision (B) = 30 / (5 + 30 + 5) = 0.75 
Recall (B) = 30 / (10 + 30 + 10) = 0.6 
F1 Score (B) = 2 × (0.75 × 0.6) / (0.75 + 0.6) 
F1 Score (B) = 2 × 0.45 / 1.35 
F1 Score (B) = 0.6666 
Precision (C) = 40 / (5 + 10 + 40) = 0.7272 
Recall (C) = 40 / (5 + 5 + 40) = 0.8 
F1 Score (C) = 2 × (0.7272 × 0.8) / (0.7272 + 0.8) 
F1 Score (C) = 2 × 0.5817 / 1.5272 
F1 Score (C) = 0.7618

Q9. 
TP = 20, FP = 10, FN = 80, TN = 890 
Total = 20 + 80 + 10 + 890 = 1000 
Accuracy = (20 + 890) / 1000 = 0.91 
Precision = 20 / (20 + 10) = 0.6666 
Recall = 20 / (20 + 80) = 0.2 
F1 Score = 2 × (0.6666 × 0.2) / (0.6666 + 0.2) 
F1 Score = 2 × 0.1333 / 0.8666 
F1 Score = 0.3076

Q10.  
TP = 45, FP = 15, FN = 5, TN = 35 
Total = 45 + 5 + 15 + 35 = 100 
Accuracy = (45 + 35) / 100 = 0.8 
Precision = 45 / (45 + 15) = 0.75 
Recall = 45 / (45 + 5) = 0.9 
F1 Score = 2 × (0.75 × 0.9) / (0.75 + 0.9) 
F1 Score = 2 × 0.675 / 1.65 
F1 Score = 0.8181
"""
