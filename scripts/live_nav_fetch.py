import requests
import pandas as pd

# Required scheme codes
scheme_codes = [
    125497,  # HDFC Top 100 Direct
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

results = []

print("=" * 60)
print("LIVE NAV FETCH")
print("=" * 60)

for code in scheme_codes:
    try:
        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        scheme_name = data["meta"]["scheme_name"]

        latest_nav = data["data"][0]["nav"]
        latest_date = data["data"][0]["date"]

        print(f"\n{scheme_name}")
        print(f"Latest NAV: {latest_nav}")
        print(f"Date: {latest_date}")

        results.append({
            "amfi_code": code,
            "scheme_name": scheme_name,
            "latest_nav": latest_nav,
            "nav_date": latest_date
        })

    except Exception as e:
        print(f"Error for scheme {code}: {e}")

# Save to CSV
df = pd.DataFrame(results)

df.to_csv(
    "data/raw/live_nav_data.csv",
    index=False
)

print("\n✅ Live NAV data saved to data/raw/live_nav_data.csv")