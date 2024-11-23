# Setting the style for seaborn
sns.set_theme(style="whitegrid")

# Line chart: Example with synthetic time-series trend
plt.figure(figsize=(10, 6))
plt.plot(range(len(df)), df["sepal length (cm)"], label="Sepal Length")
plt.plot(range(len(df)), df["sepal width (cm)"], label="Sepal Width")
plt.title("Sepal Dimensions Over Samples", fontsize=14)
plt.xlabel("Sample Index")
plt.ylabel("Sepal Dimensions (cm)")
plt.legend()
plt.show()

# Bar chart: Average petal length per species
plt.figure(figsize=(8, 6))
sns.barplot(x=grouped_data.index, y="petal length (cm)", palette="viridis")
plt.title("Average Petal Length by Species", fontsize=14)
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# Histogram: Distribution of petal width
plt.figure(figsize=(8, 6))
sns.histplot(df["petal width (cm)"], bins=20, kde=True, color="orange")
plt.title("Distribution of Petal Width", fontsize=14)
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="target", palette="cool")
plt.title("Sepal Length vs Petal Length by Species", fontsize=14)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species", labels=iris.target_names)
plt.show()
