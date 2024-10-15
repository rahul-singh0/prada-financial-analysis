import pandas as pd
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",           # Host name
    database="prada_financial_data",   # Database name
    user="rahul",               # PostgreSQL username
)

# Query to fetch data from multiple tables
query_financial = "SELECT * FROM financial_metrics"
query_regional = "SELECT * FROM regional_revenue"
query_product = "SELECT * FROM product_revenue"
query_brand = "SELECT * FROM brand_revenue"
query_sales = "SELECT * FROM sales_contribution"

# Load each table into a separate DataFrame
df_financial = pd.read_sql(query_financial, conn)
df_regional = pd.read_sql(query_regional, conn)
df_product = pd.read_sql(query_product, conn)
df_brand = pd.read_sql(query_brand, conn)
df_sales = pd.read_sql(query_sales, conn)

# Close the connection
conn.close()

# Show the first few rows of each DataFrame
print("Financial Metrics Data:")
print(df_financial.head())

print("\nRegional Revenue Data:")
print(df_regional.head())

print("\nProduct Revenue Data:")
print(df_product.head())

print("\nBrand Revenue Data:")
print(df_brand.head())

print("\nSales Contribution Data:")
print(df_sales.head())

# Check for missing values in each DataFrame
print("\nMissing values in Financial Metrics:")
print(df_financial.isnull().sum())

print("\nMissing values in Regional Revenue:")
print(df_regional.isnull().sum())

print("\nMissing values in Product Revenue:")
print(df_product.isnull().sum())

print("\nMissing values in Brand Revenue:")
print(df_brand.isnull().sum())

print("\nMissing values in Sales Contribution:")
print(df_sales.isnull().sum())

# Get a summary of each DataFrame
print("\nFinancial Metrics Data Info:")
print(df_financial.info())

print("\nRegional Revenue Data Info:")
print(df_regional.info())

print("\nProduct Revenue Data Info:")
print(df_product.info())

print("\nBrand Revenue Data Info:")
print(df_brand.info())

print("\nSales Contribution Data Info:")
print(df_sales.info())

# Make sure all expected years are present
print("\nYears in Financial Metrics:")
print(df_financial['year'].unique())

print("\nYears in Regional Revenue:")
print(df_regional['year'].unique())

print("\nYears in Product Revenue:")
print(df_product['year'].unique())

print("\nYears in Brand Revenue:")
print(df_brand['year'].unique())

print("\nYears in Sales Contribution:")
print(df_sales['year'].unique())