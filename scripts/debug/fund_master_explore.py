import pandas as pd

# Load fund master dataset
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 50)
print("FUND MASTER EXPLORATION")
print("=" * 50)

print("\nUNIQUE FUND HOUSES:")
print(fund_master["fund_house"].unique())

print("\nUNIQUE CATEGORIES:")
print(fund_master["category"].unique())

print("\nUNIQUE SUB-CATEGORIES:")
print(fund_master["sub_category"].unique())

print("\nUNIQUE RISK CATEGORIES:")
print(fund_master["risk_category"].unique())

print("\nTOTAL FUND HOUSES:")
print(fund_master["fund_house"].nunique())

print("\nTOTAL SCHEMES:")
print(len(fund_master))