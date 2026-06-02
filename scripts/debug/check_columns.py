import sqlite3

conn = sqlite3.connect("data/db/bluestock_mf.db")
cursor = conn.cursor()

cursor.execute('PRAGMA table_info("03_aum_by_fund_house")')

columns = cursor.fetchall()

print("\nColumns in 03_aum_by_fund_house:\n")

for col in columns:
    print(col)

conn.close()