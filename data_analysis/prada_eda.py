import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="prada_financial_data",
    user="rahul",  # Adjust with your PostgreSQL username
    password=""    # Leave empty if no password is needed
)

### 1. Revenue and EBITDA Trends
query_revenue_ebitda = """
SELECT year, total_revenue_million_euro, ebitda_million_euro
FROM financial_metrics
ORDER BY year;
"""
df_revenue_ebitda = pd.read_sql(query_revenue_ebitda, conn)

# Plot Revenue and EBITDA trends
plt.figure(figsize=(10, 6))
plt.plot(df_revenue_ebitda['year'], df_revenue_ebitda['total_revenue_million_euro'], label='Total Revenue (Million €)')
plt.plot(df_revenue_ebitda['year'], df_revenue_ebitda['ebitda_million_euro'], label='EBITDA (Million €)')
plt.title('Revenue and EBITDA Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Million €')
plt.legend()
plt.grid(True)
plt.show()

### 2. Regional Revenue Performance
query_regional = """
SELECT year, region, revenue_million_euro
FROM regional_revenue
ORDER BY year, region;
"""
df_regional = pd.read_sql(query_regional, conn)

# Pivot the DataFrame for plotting regional revenue trends
df_regional_pivot = df_regional.pivot(index='year', columns='region', values='revenue_million_euro')

# Plot Regional Revenue Performance (Stacked Area Plot)
df_regional_pivot.plot(kind='area', stacked=True, figsize=(10, 6))
plt.title('Regional Revenue Performance Over Time')
plt.xlabel('Year')
plt.ylabel('Revenue (Million €)')
plt.legend(title='Region')
plt.grid(True)
plt.show()

### 3. Product Category Revenue
query_product = """
SELECT year, product_category, revenue_million_euro
FROM product_revenue
ORDER BY year, product_category;
"""
df_product = pd.read_sql(query_product, conn)

# Pivot the DataFrame for plotting product category trends
df_product_pivot = df_product.pivot(index='year', columns='product_category', values='revenue_million_euro')

# Plot Product Category Revenue (Stacked Bar Plot)
df_product_pivot.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Product Category Revenue Over Time')
plt.xlabel('Year')
plt.ylabel('Revenue (Million €)')
plt.legend(title='Product Category')
plt.grid(True)
plt.show()

### 4. Year-over-Year (YoY) Growth in Revenue and EBITDA
query_yoy_growth = """
WITH revenue_ebitda_growth AS (
    SELECT year, 
           total_revenue_million_euro,
           LAG(total_revenue_million_euro) OVER (ORDER BY year) AS prev_year_revenue,
           ebitda_million_euro,
           LAG(ebitda_million_euro) OVER (ORDER BY year) AS prev_year_ebitda
    FROM financial_metrics
)
SELECT year,
       (total_revenue_million_euro - prev_year_revenue) / prev_year_revenue * 100 AS yoy_revenue_growth,
       (ebitda_million_euro - prev_year_ebitda) / prev_year_ebitda * 100 AS yoy_ebitda_growth
FROM revenue_ebitda_growth
WHERE prev_year_revenue IS NOT NULL;
"""
df_yoy_growth = pd.read_sql(query_yoy_growth, conn)

# Plot Year-over-Year Growth for Revenue and EBITDA
plt.figure(figsize=(10, 6))
plt.plot(df_yoy_growth['year'], df_yoy_growth['yoy_revenue_growth'], label='YoY Revenue Growth')
plt.plot(df_yoy_growth['year'], df_yoy_growth['yoy_ebitda_growth'], label='YoY EBITDA Growth')
plt.title('Year-over-Year Growth in Revenue and EBITDA')
plt.xlabel('Year')
plt.ylabel('Growth (%)')
plt.legend()
plt.grid(True)
plt.show()

### 5. Net Income and Net Income Margin
query_net_income = """
SELECT year, net_income_million_euro, 
       net_income_million_euro / total_revenue_million_euro * 100 AS net_income_margin
FROM financial_metrics
ORDER BY year;
"""
df_net_income = pd.read_sql(query_net_income, conn)

# Plot Net Income and Net Income Margin
plt.figure(figsize=(10, 6))
plt.plot(df_net_income['year'], df_net_income['net_income_million_euro'], label='Net Income (Million €)')
plt.title('Net Income Over Time')
plt.xlabel('Year')
plt.ylabel('Net Income (Million €)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df_net_income['year'], df_net_income['net_income_margin'], label='Net Income Margin (%)')
plt.title('Net Income Margin Over Time')
plt.xlabel('Year')
plt.ylabel('Percentage (%)')
plt.grid(True)
plt.show()

### 6. Store Performance: Total Stores Over Time
query_stores = """
SELECT year, total_stores
FROM financial_metrics
ORDER BY year;
"""
df_stores = pd.read_sql(query_stores, conn)

# Plot Total Stores Over Time
plt.figure(figsize=(10, 6))
plt.plot(df_stores['year'], df_stores['total_stores'], label='Total Stores')
plt.title('Total Stores Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Stores')
plt.grid(True)
plt.show()

### 7. Retail vs Wholesale Sales Contribution
query_sales_contribution = """
SELECT year, retail_sales_percent, wholesale_sales_percent
FROM sales_contribution
ORDER BY year;
"""
df_sales_contribution = pd.read_sql(query_sales_contribution, conn)

# Plot Retail vs Wholesale Sales Contribution
df_sales_contribution.plot(x='year', y=['retail_sales_percent', 'wholesale_sales_percent'], kind='bar', figsize=(10, 6), stacked=True)
plt.title('Retail vs Wholesale Sales Contribution Over Time')
plt.xlabel('Year')
plt.ylabel('Percentage (%)')
plt.grid(True)
plt.show()

### 8. Revenue Per Store
query_rev_per_store = """
SELECT year, total_revenue_million_euro / total_stores AS avg_revenue_per_store_million_euro
FROM financial_metrics
ORDER BY year;
"""
df_rev_per_store = pd.read_sql(query_rev_per_store, conn)

# Plot Revenue Per Store Over Time
plt.figure(figsize=(10, 6))
plt.plot(df_rev_per_store['year'], df_rev_per_store['avg_revenue_per_store_million_euro'], label='Average Revenue Per Store (Million €)')
plt.title('Revenue Per Store Over Time')
plt.xlabel('Year')
plt.ylabel('Million €')
plt.grid(True)
plt.show()

### 9. Brand Performance
query_brand = """
SELECT year, brand, revenue_million_euro
FROM brand_revenue
ORDER BY year, brand;
"""
df_brand = pd.read_sql(query_brand, conn)

# Pivot the DataFrame for plotting brand performance
df_brand_pivot = df_brand.pivot(index='year', columns='brand', values='revenue_million_euro')

# Plot Brand Performance Over Time
df_brand_pivot.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Brand Performance Over Time')
plt.xlabel('Year')
plt.ylabel('Revenue (Million €)')
plt.legend(title='Brand')
plt.grid(True)
plt.show()

# Close the connection
conn.close()