# Bluestock Mutual Fund Capstone Project

## 📊 Overview
This project is a complete data engineering and analytics pipeline for mutual fund data analysis using Python, SQLite, and Matplotlib.

---

## ⚙️ Tech Stack
- Python
- Pandas
- SQLite
- Matplotlib

---

## 📂 Project Structure
- data/raw → Raw CSV files
- data/db → SQLite database
- sql → SQL queries
- scripts → ETL + dashboard scripts

---

## 🔄 ETL Pipeline
- Extract: Load CSV files using pandas
- Transform: Clean and standardize data
- Load: Store into SQLite database

---

## 📈 Key Analysis
- SIP inflow trends
- AUM analysis by fund house
- Category-wise inflows
- Mutual fund performance ranking

---

## 📊 Dashboard
Generated visual insights:
- Monthly SIP trends
- Fund house AUM comparison
- Category inflow distribution
- Top performing schemes

---

## 🧠 Key Insights
- SIP inflows show consistent growth trend
- Equity categories dominate inflows
- Top fund houses hold highest AUM concentration
- High return schemes show higher volatility

---

## 🚀 How to Run
```bash
python scripts/etl_pipeline.py
python scripts/dashboard.py