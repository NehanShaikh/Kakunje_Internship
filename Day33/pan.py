# PANDAS TASKS
import pandas as pd

# Task 1
df = pd.DataFrame({
    "Name":["Asha","Ravi","John","Meena"],
    "Marks":[85,90,78,88]
})
print(df)

# Task 2
df["Grade"] = ["A","A+","B","A"]
print(df)

# Task 3
sorted_df = df.sort_values(by="Marks")
print(sorted_df)

# Task 4
data = pd.read_csv("employee_data.csv")
print(data.head(25))

# Task 5
clean = data.dropna()
print(clean)

# Task 6
data.fillna(data.median(numeric_only=True), inplace=True)
print(data)
