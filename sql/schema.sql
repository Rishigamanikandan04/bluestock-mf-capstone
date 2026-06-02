CREATE TABLE IF NOT EXISTS mutual_funds (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_name TEXT,
    category TEXT,
    nav REAL,
    expense_ratio REAL,
    returns_1yr REAL,
    returns_3yr REAL,
    returns_5yr REAL,
    risk_level TEXT,
    last_updated DATE
);