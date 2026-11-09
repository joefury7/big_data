-- ================================================================================
-- BIG DATA SYSTEMS (24CI51) - SELF LEARNING ACTIVITY 1: APACHE HIVE
-- Student Name : Joel B John
-- USN          : 1MS24CI060
-- Department   : CSE (Artificial Intelligence & Machine Learning)
-- File         : hive_queries.sql
-- ================================================================================

-- 1. Create Dedicated Database
CREATE DATABASE IF NOT EXISTS jbj_mart_db_060;
USE jbj_mart_db_060;

-- 2. Create Staging External Table (Schema-on-Read over raw CSV)
CREATE EXTERNAL TABLE IF NOT EXISTS staging_sales_060 (
    transaction_id STRING,
    customer_id STRING,
    branch_code STRING,
    branch_city STRING,
    product_id STRING,
    product_name STRING,
    category STRING,
    unit_price DOUBLE,
    quantity INT,
    total_amount DOUBLE,
    payment_mode STRING,
    transaction_timestamp STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hadoop/retail/staging_060'
TBLPROPERTIES ("skip.header.line.count"="1");

-- 3. Create Production Managed Partitioned Table (Optimized Row Columnar - ORC)
CREATE TABLE IF NOT EXISTS sales_partitioned_060 (
    transaction_id STRING,
    customer_id STRING,
    branch_city STRING,
    product_id STRING,
    product_name STRING,
    category STRING,
    unit_price DOUBLE,
    quantity INT,
    total_amount DOUBLE,
    payment_mode STRING,
    transaction_timestamp TIMESTAMP
)
PARTITIONED BY (branch_code STRING)
STORED AS ORC
TBLPROPERTIES ("orc.compress"="SNAPPY");

-- 4. Enable Dynamic Partitioning and Ingest from Staging Table
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

INSERT OVERWRITE TABLE sales_partitioned_060 PARTITION (branch_code)
SELECT 
    transaction_id,
    customer_id,
    branch_city,
    product_id,
    product_name,
    category,
    unit_price,
    quantity,
    total_amount,
    payment_mode,
    CAST(transaction_timestamp AS TIMESTAMP),
    branch_code
FROM staging_sales_060;

-- ================================================================================
-- 5. ANALYTICAL BUSINESS QUERIES
-- ================================================================================

-- Query 1: Branch-wise Sales Revenue & Contribution Percentage
SELECT 
    branch_code,
    branch_city,
    COUNT(transaction_id) AS total_orders,
    ROUND(SUM(total_amount), 2) AS branch_revenue_inr,
    ROUND(AVG(total_amount), 2) AS avg_ticket_size_inr,
    ROUND(SUM(total_amount) * 100.0 / SUM(SUM(total_amount)) OVER(), 2) AS revenue_share_pct
FROM sales_partitioned_060
GROUP BY branch_code, branch_city
ORDER BY branch_revenue_inr DESC;

-- Query 2: Top 5 Best-Selling Products and Category Revenue
SELECT 
    category,
    product_name,
    SUM(quantity) AS units_sold,
    ROUND(SUM(total_amount), 2) AS total_sales_inr
FROM sales_partitioned_060
GROUP BY category, product_name
ORDER BY units_sold DESC
LIMIT 5;

-- Query 3: Peak Sales Hours Analysis (Hourly Transaction Density)
SELECT 
    HOUR(transaction_timestamp) AS hour_of_day,
    COUNT(transaction_id) AS transaction_count,
    ROUND(SUM(total_amount), 2) AS hourly_revenue_inr
FROM sales_partitioned_060
GROUP BY HOUR(transaction_timestamp)
ORDER BY transaction_count DESC;

-- Query 4: Monthly Sales Turnover Trends (Jan 2026 - Apr 2026)
SELECT 
    DATE_FORMAT(transaction_timestamp, 'yyyy-MM') AS sales_month,
    COUNT(transaction_id) AS total_transactions,
    SUM(quantity) AS total_items_sold,
    ROUND(SUM(total_amount), 2) AS gross_monthly_revenue_inr
FROM sales_partitioned_060
GROUP BY DATE_FORMAT(transaction_timestamp, 'yyyy-MM')
ORDER BY sales_month ASC;
