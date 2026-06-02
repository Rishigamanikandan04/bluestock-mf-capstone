-- =====================================================
-- BLUESTOCK MF CAPSTONE - FINAL ANALYSIS QUERIES
-- =====================================================

-- =========================
-- 1. LIST ALL TABLES
-- =========================
SELECT name 
FROM sqlite_master 
WHERE type='table';


-- =========================
-- 2. FUND MASTER DATA
-- =========================
SELECT *
FROM "01_fund_master"
LIMIT 10;


-- =========================
-- 3. NAV HISTORY ANALYSIS
-- =========================
SELECT *
FROM "02_nav_history"
LIMIT 10;

-- Top NAV funds
SELECT *
FROM "02_nav_history"
ORDER BY nav DESC
LIMIT 10;

-- Lowest NAV funds
SELECT *
FROM "02_nav_history"
ORDER BY nav ASC
LIMIT 10;


-- =========================
-- 4. AUM BY FUND HOUSE
-- =========================
-- Top fund houses by AUM
SELECT 
    date,
    fund_house,
    aum_lakh_crore,
    num_schemes
FROM "03_aum_by_fund_house"
ORDER BY aum_lakh_crore DESC
LIMIT 10;


-- =========================
-- 5. SIP INFLOWS
-- =========================
-- Full SIP dataset
SELECT *
FROM "04_monthly_sip_inflows"
ORDER BY month;

-- Top SIP inflow months
SELECT 
    month,
    sip_inflow_crore
FROM "04_monthly_sip_inflows"
ORDER BY sip_inflow_crore DESC
LIMIT 10;

-- SIP growth trend
SELECT 
    month,
    yoy_growth_pct
FROM "04_monthly_sip_inflows"
ORDER BY yoy_growth_pct DESC
LIMIT 10;


-- =========================
-- 6. CATEGORY INFLOWS
-- =========================
-- Category trend
SELECT 
    month,
    category,
    net_inflow_crore
FROM "05_category_inflows"
ORDER BY month, net_inflow_crore DESC;

-- Category total inflow
SELECT 
    category,
    SUM(net_inflow_crore) AS total_inflow
FROM "05_category_inflows"
GROUP BY category
ORDER BY total_inflow DESC;


-- =========================
-- 7. INDUSTRY FOLIO COUNT
-- =========================

-- Full trend
SELECT *
FROM "06_industry_folio_count"
ORDER BY month;


-- Total folios trend
SELECT 
    month,
    total_folios_crore
FROM "06_industry_folio_count"
ORDER BY month;


-- Equity vs Debt comparison
SELECT 
    month,
    equity_folios_crore,
    debt_folios_crore
FROM "06_industry_folio_count"
ORDER BY month;


-- Category breakdown snapshot
SELECT 
    month,
    equity_folios_crore,
    debt_folios_crore,
    hybrid_folios_crore,
    others_folios_crore
FROM "06_industry_folio_count"
ORDER BY month;

-- =========================
-- 8. SCHEME PERFORMANCE
-- =========================

-- Full dataset sample
SELECT *
FROM "07_scheme_performance"
LIMIT 10;


-- Top performing schemes (1 year return)
SELECT 
    scheme_name,
    fund_house,
    category,
    return_1yr_pct,
    return_3yr_pct,
    return_5yr_pct,
    risk_grade
FROM "07_scheme_performance"
ORDER BY return_1yr_pct DESC
LIMIT 10;


-- Best long term performers (5 year)
SELECT 
    scheme_name,
    fund_house,
    return_5yr_pct,
    sharpe_ratio,
    max_drawdown_pct
FROM "07_scheme_performance"
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- High risk vs high return analysis
SELECT 
    scheme_name,
    return_1yr_pct,
    risk_grade,
    beta,
    sharpe_ratio
FROM "07_scheme_performance"
ORDER BY return_1yr_pct DESC
LIMIT 10;


-- Best risk-adjusted returns (Sharpe ratio)
SELECT 
    scheme_name,
    return_1yr_pct,
    sharpe_ratio,
    sortino_ratio
FROM "07_scheme_performance"
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- =========================
-- 9. INVESTOR TRANSACTIONS
-- =========================
SELECT *
FROM "08_investor_transactions"
LIMIT 10;


-- =========================
-- 10. PORTFOLIO HOLDINGS
-- =========================
SELECT *
FROM "09_portfolio_holdings"
LIMIT 10;


-- =========================
-- 11. BENCHMARK INDICES
-- =========================
SELECT *
FROM "10_benchmark_indices"
LIMIT 10;


-- =========================
-- 12. LIVE NAV DATA
-- =========================
SELECT *
FROM "live_nav_data"
LIMIT 10;