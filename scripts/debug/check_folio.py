import sqlite3

conn = sqlite3.connect("data/db/bluestock_mf.db")
cursor = conn.cursor()

cursor.execute('PRAGMA table_info("06_industry_folio_count")')
columns = cursor.fetchall()

print("\n06_industry_folio_count columns:\n")

for col in columns:
    print(col)

conn.close()