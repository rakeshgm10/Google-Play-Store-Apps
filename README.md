# Google Play Store Analysis

## Project Overview
This project focuses on analyzing the Google Play Store dataset to gain insights into app ratings, categories, and trends. It includes data cleaning, exploratory data analysis (EDA), machine learning modeling, and storing results in SQL.

## Features
- **Data Cleaning**: Preprocess raw Google Play Store data
- **Exploratory Data Analysis (EDA)**: Generate insights and visualizations
- **Machine Learning Model**: Predict app ratings
- **SQL Integration**: Store and query cleaned data
- **Automated Execution**: `run_all.bat` to execute scripts in sequence

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/playstore-analysis.git
   ```
2. Navigate to the project folder:
   ```bash
   cd playstore
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- Run data cleaning:
  ```bash
  python data_cleaning.py
  ```
- Perform EDA:
  ```bash
  python eda.py
  ```
- Train ML model:
  ```bash
  python ml_model.py
  ```
- Export data to SQL:
  ```bash
  python store_to_sql.py
  ```
- Execute all scripts:
  ```bash
  run_all.bat  # Windows only
  ```

## Data
- `googleplaystore.csv.xlsx`: Raw dataset
- `googleplaystore_cleaned.csv`: Processed dataset
- `googleplaystore_final.csv`: Final dataset after transformations
- `playstore_analysis.xlsx`: Analysis results

## Visualizations
- `ratings_distribution.png`: Distribution of app ratings
- `top_categories.png`: Top categories of apps

## License
This project is licensed under the MIT License.

## Author
RAKESH M - [rakeshgm2024@gmail.com]
