"""
Task 12
Load CSV file and perform: (you can use data.csv or any other csv files if you have)
1.	Show first 5 rows
2.	Show last 5 rows
3.	Show column names
4.	Remove null values
5.	Replace null values with mean
"""

import pandas as pd

df = pd.read_csv("Students.csv")

print("First 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nColumn Names:")
print(df.columns)

df_no_null = df.dropna()
print("\nData after removing null values:")
print(df_no_null)

df_filled = df.fillna(df.mean(numeric_only=True))
print("\nData after replacing null values with mean:")
print(df_filled)
