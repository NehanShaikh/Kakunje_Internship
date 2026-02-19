import pandas as pd
import numpy as np

df = pd.read_csv("Students.csv")

print(df, "\n")

print(df.describe(include='all'),"\n")

print(df['age'],"\n")

df.rename(columns={'age': 'student_age'}, inplace=True)
print(df.columns,"\n")

df['marks'] = pd.to_numeric(df['marks'], errors='coerce')

mean_marks = df['marks'].mean()
df['marks'] = df['marks'].fillna(mean_marks)

median_age = df['student_age'].median()
df['student_age'] = df['student_age'].fillna(median_age)

df = df.drop_duplicates()

print(df, "\n")

print(df.head(5),"\n")

print(df.tail(5),"\n")

print(df.sample(3),"\n")

df_cleaned = df.dropna()

print(df_cleaned, "\n")

df_cleaned.to_csv("Cleaned_Students.csv", index=False)
