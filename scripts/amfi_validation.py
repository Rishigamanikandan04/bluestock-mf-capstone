import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Get unique AMFI codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = master_codes - nav_codes

print("=" * 50)
print("AMFI CODE VALIDATION")
print("=" * 50)

print(f"Fund Master Codes: {len(master_codes)}")
print(f"NAV History Codes: {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\n✅ SUCCESS: All AMFI codes in fund_master exist in nav_history.")
else:
    print("\n❌ Missing AMFI Codes:")
    print(missing_codes)