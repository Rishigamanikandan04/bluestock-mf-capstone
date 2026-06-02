import sqlite3

DB_PATH = "data/db/bluestock_mf.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 1. Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("\nTables in database:")
for t in tables:
    print("-", t[0])

# 2. Check row count for each table
print("\nRow counts:")
for t in tables:
    table_name = t[0]
    cursor.execute(f'SELECT COUNT(*) FROM "{table_name}"')
    count = cursor.fetchone()[0]
    print(f"{table_name}: {count} rows")

conn.close()