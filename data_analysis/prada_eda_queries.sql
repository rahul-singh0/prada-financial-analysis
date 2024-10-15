-- Calculate revenue per store over time
SELECT year, 
    ROUND(total_revenue_million_euro / total_stores, 2) AS avg_revenue_per_store_million_euro 
FROM financial_metrics
ORDER BY year;

-- Track revenue performance for different brands over time
SELECT year, brand, revenue_million_euro 
FROM brand_revenue
ORDER BY year, brand;

-- Calculate year-on-year growth for total revenue and EBITDA
WITH revenue_ebitda_growth AS (
    SELECT year, 
        total_revenue_million_euro, 
        LAG(total_revenue_million_euro) OVER (ORDER BY year) AS prev_year_revenue, 
        ebitda_million_euro, 
        LAG(ebitda_million_euro) OVER (ORDER BY year) AS prev_year_ebitda 
    FROM financial_metrics
)
SELECT year, 
    ROUND((total_revenue_million_euro - prev_year_revenue) / prev_year_revenue * 100, 2) AS yoy_revenue_growth, 
    ROUND((ebitda_million_euro - prev_year_ebitda) / prev_year_ebitda * 100, 2) AS yoy_ebitda_growth
FROM revenue_ebitda_growth
WHERE prev_year_revenue IS NOT NULL;

-- Track net income and profit margin over time
SELECT year, net_income_million_euro, 
    ROUND(net_income_million_euro / total_revenue_million_euro * 100, 2) AS net_income_margin 
FROM financial_metrics
ORDER BY year;

-- Track the total number of stores over time
SELECT year, total_stores 
FROM financial_metrics
ORDER BY year;

-- Analyse retail vs wholesale contributions to revenue
SELECT year, retail_sales_percent, wholesale_sales_percent 
FROM sales_contribution
ORDER BY year;

-- Track total revenue and EBITDA over time to analyse financial growth
SELECT year, total_revenue_million_euro, ebitda_million_euro 
FROM financial_metrics
ORDER BY year;

-- Track revenue across different regions over time
SELECT year, region, revenue_million_euro 
FROM regional_revenue
ORDER BY year, region;

-- Analyse revenue from different product categories over time
SELECT year, product_category, revenue_million_euro 
FROM product_revenue
ORDER BY year, product_category;