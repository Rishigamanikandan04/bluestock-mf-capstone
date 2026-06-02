import sqlite3

conn = sqlite3.connect("data/db/bluestock_mf.db")
cursor = conn.cursor()

cursor.execute('PRAGMA table_info("04_monthly_sip_inflows")')
columns = cursor.fetchall()

print("\n04_monthly_sip_inflows columns:\n")

for col in columns:
    print(col)

conn.close()