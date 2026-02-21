# Task11
import numpy as np
import pandas as pd

marks = np.array([85, 90, 78, 90, 85, 88])

arr2d = marks.reshape(3,2)
print("2D Array:\n", arr2d)

df = pd.DataFrame(arr2d, columns=["Maths", "Science"])

df.loc[1, "Science"] = np.nan

df["Science"] = df["Science"].fillna(df["Science"].mean())

df = df.drop_duplicates()

print("\nCleaned DataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())
