import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "data/db/bluestock_mf.db"
conn = sqlite3.connect(DB_PATH)

sip_df = pd.read_sql('SELECT * FROM "04_monthly_sip_inflows"', conn)
aum_df = pd.read_sql('SELECT * FROM "03_aum_by_fund_house"', conn)
cat_df = pd.read_sql('SELECT * FROM "05_category_inflows"', conn)
scheme_df = pd.read_sql('SELECT * FROM "07_scheme_performance"', conn)

# =========================
# 1. SIP TREND
# =========================
plt.figure(figsize=(8,4))
plt.plot(sip_df["month"], sip_df["sip_inflow_crore"], marker='o')
plt.title("Monthly SIP Inflow Trend")
plt.xlabel("Month")
plt.ylabel("SIP Inflow (Crore)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/charts/sip_trend.png")
plt.show()
plt.close()

# =========================
# 2. AUM TREND
# =========================
top_aum = aum_df.groupby("fund_house")["aum_lakh_crore"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,4))
top_aum.plot(kind='bar')
plt.title("Top Fund Houses by AUM")
plt.xlabel("Fund House")
plt.ylabel("AUM (Lakh Crore)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/charts/aum_ranking.png")
plt.show()
plt.close()

# =========================
# 3. CATEGORY INFLOWS
# =========================
cat_group = cat_df.groupby("category")["net_inflow_crore"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,4))
cat_group.plot(kind='bar')
plt.title("Category Wise Net Inflows")
plt.xlabel("Category")
plt.ylabel("Net Inflow (Crore)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/charts/category_inflows.png")
plt.show()
plt.close()

# =========================
# 4. TOP SCHEMES
# =========================
top_schemes = scheme_df.sort_values("return_1yr_pct", ascending=False).head(10)

plt.figure(figsize=(8,4))
plt.bar(top_schemes["scheme_name"], top_schemes["return_1yr_pct"])
plt.title("Top Schemes by 1-Year Return")
plt.xlabel("Scheme")
plt.ylabel("Return %")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("reports/charts/top_schemes.png")
plt.show()
plt.close()

conn.close()