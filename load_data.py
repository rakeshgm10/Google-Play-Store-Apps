import pandas as pd

# Load the data from the Excel file
excel_file = "googleplaystore.csv.xlsx"
df = pd.read_excel(excel_file)

print("✅ Data loaded successfully!")

# Perform basic cleaning (remove duplicates, missing values, etc.)
df.drop_duplicates(inplace=True)  # Remove duplicate rows
df.dropna(inplace=True)  # Remove rows with missing values

# Save the cleaned data to a new CSV file
cleaned_file = "googleplaystore_cleaned.csv"
df.to_csv(cleaned_file, index=False)

print(f"✅ Cleaned data saved to {cleaned_file}")
