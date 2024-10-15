-- Create Database prada_financial_data
CREATE DATABASE prada_financial_data;

CREATE TABLE financial_metrics (
    year INT PRIMARY KEY,
    total_revenue_million_euro DECIMAL(10,2),
    ebitda_million_euro DECIMAL(10,2),
    net_income_million_euro DECIMAL(10,2),
    gross_margin_percent DECIMAL(5,2),
    ebit_million_euro DECIMAL(10,2),
    ebitda_margin_percent DECIMAL(5,2),
    total_stores INT
);

--Create tables for database
CREATE TABLE regional_revenue (
    year INT,
    region VARCHAR(50),
    revenue_million_euro DECIMAL(10,2),
    PRIMARY KEY (year, region),
    FOREIGN KEY (year) REFERENCES financial_metrics(year)
);

CREATE TABLE product_revenue (
    year INT,
    product_category VARCHAR(50),
    revenue_million_euro DECIMAL(10,2),
    PRIMARY KEY (year, product_category),
    FOREIGN KEY (year) REFERENCES financial_metrics(year)
);

CREATE TABLE brand_revenue (
    year INT,
    brand VARCHAR(50),
    revenue_million_euro DECIMAL(10,2),
    PRIMARY KEY (year, brand),
    FOREIGN KEY (year) REFERENCES financial_metrics(year)
);

CREATE TABLE sales_contribution (
    year INT PRIMARY KEY,
    retail_sales_percent DECIMAL(5,2),
    wholesale_sales_percent DECIMAL(5,2),
    FOREIGN KEY (year) REFERENCES financial_metrics(year)
);

--Copy CSV data into tables

COPY financial_metrics FROM '/Users/rahul/Documents/Analyst/Projects/Prada Financial Analysis/Annual Reports/Tables/csv/financial_metrics.csv' DELIMITER ',' CSV HEADER;

COPY regional_revenue FROM '/Users/rahul/Documents/Analyst/Projects/Prada Financial Analysis/Annual Reports/Tables/csv/regional_revenue.csv' DELIMITER ',' CSV HEADER;

COPY product_revenue FROM '/Users/rahul/Documents/Analyst/Projects/Prada Financial Analysis/Annual Reports/Tables/csv/product_revenue.csv' DELIMITER ',' CSV HEADER;

COPY brand_revenue FROM '/Users/rahul/Documents/Analyst/Projects/Prada Financial Analysis/Annual Reports/Tables/csv/brand_revenue.csv' DELIMITER ',' CSV HEADER;

COPY sales_contribution FROM '/Users/rahul/Documents/Analyst/Projects/Prada Financial Analysis/Annual Reports/Tables/csv/sales_contribution.csv' DELIMITER ',' CSV HEADER;