# Task1
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips.head())
print(tips.info())


# Task2
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.title("Total Bill vs Tip")
plt.show()

avg_tip = tips.groupby("day")["tip"].mean().reset_index()

sns.lineplot(data=avg_tip, x="day", y="tip", marker="o")
plt.title("Average Tip per Day")
plt.show()

sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average Total Bill by Day")
plt.show()

sns.histplot(tips["total_bill"], kde=True)
plt.title("Distribution of Total Bill")
plt.show()


# Task3
fig, axes = plt.subplots(2, 1, figsize=(6,8))

sns.scatterplot(data=tips, x="total_bill", y="tip", ax=axes[0])
axes[0].set_title("Scatter Plot")

sns.histplot(tips["total_bill"], ax=axes[1])
axes[1].set_title("Histogram")

plt.tight_layout()
plt.show()


# Task4
corr = tips.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# Task5
titanic = sns.load_dataset("titanic")

sns.countplot(data=titanic, x="survived")
plt.title("Survival Count")
plt.show()

sns.histplot(titanic["age"], kde=True)
plt.title("Age Distribution")
plt.show()

sns.countplot(data=titanic, x="sex", hue="survived")
plt.title("Survival by Gender")
plt.show()

corr = titanic.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="viridis")
plt.title("Titanic Correlation Heatmap")
plt.show()
