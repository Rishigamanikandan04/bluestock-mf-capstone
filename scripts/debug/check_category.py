import sqlite3

conn = sqlite3.connect("data/db/bluestock_mf.db")
cursor = conn.cursor()

cursor.execute('PRAGMA table_info("05_category_inflows")')
columns = cursor.fetchall()

print("\nCategory inflows columns:\n")

for col in columns:
    print(col)

conn.close()