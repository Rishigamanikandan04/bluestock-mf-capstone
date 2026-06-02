import sqlite3

conn = sqlite3.connect("data/db/bluestock_mf.db")
cursor = conn.cursor()

cursor.execute('PRAGMA table_info("07_scheme_performance")')
columns = cursor.fetchall()

print("\n07_scheme_performance columns:\n")

for col in columns:
    print(col)

conn.close()