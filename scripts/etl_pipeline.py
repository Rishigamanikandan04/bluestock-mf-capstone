import sqlite3
import pandas as pd
from pathlib import Path

# Paths
DB_PATH = "data/db/bluestock_mf.db"
RAW_FOLDER = Path("data/raw")

# Connect DB
conn = sqlite3.connect(DB_PATH)

print("Connected to database")

# Loop through all CSV files
for file in RAW_FOLDER.glob("*.csv"):
    print(f"Processing {file.name}")

    # Read CSV
    df = pd.read_csv(file)

    # Basic cleaning
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df = df.drop_duplicates()

    # Table name = file name
    table_name = file.stem.lower()

    # Load into SQLite
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    print(f"Loaded {table_name} successfully")

conn.close()

print("ETL Completed Successfully!")