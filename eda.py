import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("googleplaystore_final.csv")

# Rating distribution
sns.histplot(df['Rating'].dropna(), bins=20, kde=True)
plt.title("App Ratings Distribution")
plt.savefig("ratings_distribution.png")
plt.show()

# Most popular app categories
df['Category'].value_counts().head(10).plot(kind='bar', title="Top 10 Categories")
plt.savefig("top_categories.png")
plt.show()
