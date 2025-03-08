import pandas as pd

# Load final dataset
df = pd.read_csv("googleplaystore_final.csv")

# Export to Excel
df.to_excel("playstore_analysis.xlsx", index=False)

print("Data exported to playstore_analysis.xlsx")
