from sqlalchemy import create_engine
import pandas as pd


# Use correct credentials (replace with actual values)
username = "root"        # MySQL username (keep it as a string)
password = "rakesh"  # Replace with your actual MySQL root password
host = "localhost"       # Use 'localhost' or '127.0.0.1'
database = "playstore_db"  # Change to your actual database name

# Correct connection string
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

print("MySQL Connection Successful!")

