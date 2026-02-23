"""
Task 11

Create DataFrame:

Name
A
B
C

Marks
85
90
78

Age
20
21
19

Print first row
Print Marks columm
"""

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 78],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)

print("First Row:")
print(df.iloc[0])

print("\nMarks Column:")
print(df["Marks"])
