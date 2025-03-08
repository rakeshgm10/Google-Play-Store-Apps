import pandas as pd

# Load dataset
df = pd.read_csv("googleplaystore_cleaned.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert 'Installs' column to numeric
df['Installs'] = df['Installs'].str.replace(r'[+,]', '', regex=True).astype(int)

# Convert 'Price' column to numeric (remove '$' sign)
df['Price'] = df['Price'].str.replace('$', '').astype(float)

# Handle missing values
df.fillna(df.select_dtypes(include=['number']).median(), inplace=True)


# Save cleaned dataset
df.to_csv("googleplaystore_final.csv", index=False)

print("Data cleaning complete. File saved as googleplaystore_final.csv")
