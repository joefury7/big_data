"""
================================================================================
  BIG DATA SYSTEMS (24CI51) - ACTIVITY 1: REAL APACHE HIVE WAREHOUSE
  Student Name : Joel B John
  USN          : 1MS24CI060
  Department   : CSE (Artificial Intelligence & Machine Learning)
  Institution  : Ramaiah Institute of Technology (MSRIT)
  File         : real_hive_job.py
================================================================================
Production Apache Hive / Spark SQL Data Warehouse pipeline running over
real Hadoop Distributed File System (HDFS):
1. Ingests raw sales dataset from hdfs://localhost:9000/...
2. Creates Hive external staging table and managed partitioned ORC table
3. Executes 4 business analytical queries
4. Validates HDFS physical partitions and storage blocks
================================================================================
"""

import sys
import os
import subprocess
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, to_timestamp, date_format, sum as _sum, count as _count, avg as _avg, round as _round

HDFS_BASE = "hdfs://localhost:9000"
HDFS_RAW_PATH = f"{HDFS_BASE}/user/joel/retail_warehouse_1MS24CI060/raw_sales"
DB_NAME = "hive_retail_1MS24CI060"

def print_banner():
    print("=" * 85)
    print("      DEPARTMENT OF CSE (ARTIFICIAL INTELLIGENCE & MACHINE LEARNING)        ")
    print("         BIG DATA SYSTEMS (24CI51) - ACTIVITY 1: REAL APACHE HIVE           ")
    print("      REAL HADOOP HDFS STORAGE + APACHE HIVE METASTORE & QUERY PLANNER       ")
    print("   Student: Joel B John  |  USN: 1MS24CI060  |  Institution: MSRIT           ")
    print("=" * 85 + "\n")

def main():
    print_banner()

    print(f"[*] Initializing SparkSession with native Hive Metastore support...")
    print(f"    - Target HDFS Warehouse Dir: {HDFS_BASE}/user/hive/warehouse")
    print(f"    - Target Database Name      : {DB_NAME}\n")

    spark = SparkSession.builder \
        .appName("Hive_Warehouse_Analytics_1MS24CI060") \
        .master("local[*]") \
        .config("spark.sql.warehouse.dir", f"{HDFS_BASE}/user/hive/warehouse") \
        .config("spark.hadoop.fs.defaultFS", HDFS_BASE) \
        .config("spark.sql.catalogImplementation", "hive") \
        .enableHiveSupport() \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # 1. Create Hive Database
    print(f"[*] Step 1: Creating real Hive Database '{DB_NAME}' on HDFS...")
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    spark.sql(f"USE {DB_NAME}")

    # 2. Create Staging Table directly pointing to HDFS directory
    print(f"[*] Step 2: Creating External Hive Staging Table backed by HDFS...")
    spark.sql("DROP TABLE IF EXISTS staging_sales_060")
    spark.sql(f"""
        CREATE EXTERNAL TABLE staging_sales_060 (
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
        LOCATION '{HDFS_RAW_PATH}'
        TBLPROPERTIES ('skip.header.line.count'='1')
    """)

    staging_count = spark.sql("SELECT COUNT(*) FROM staging_sales_060").collect()[0][0]
    print(f"[OK] Hive Staging Table successfully mounted over HDFS raw files: {staging_count:,} records found.\n")

    # 3. Create Managed Partitioned Hive Table in ORC Format
    print(f"[*] Step 3: Creating Managed Partitioned Hive Table (Stored as ORC, Partitioned by branch_code)...")
    spark.sql("DROP TABLE IF EXISTS sales_partitioned_060")
    spark.sql("""
        CREATE TABLE sales_partitioned_060 (
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
    """)

    # Populate partitioned table from staging (filter out CSV header)
    print(f"[*] Step 4: Executing dynamic partition ingestion into HDFS warehouse...")
    spark.sql("""
        INSERT OVERWRITE TABLE sales_partitioned_060 PARTITION (branch_code)
        SELECT 
            transaction_id,
            customer_id,
            branch_city,
            product_id,
            product_name,
            category,
            CAST(unit_price AS DOUBLE),
            CAST(quantity AS INT),
            CAST(total_amount AS DOUBLE),
            payment_mode,
            TO_TIMESTAMP(transaction_timestamp, 'yyyy-MM-dd HH:mm:ss'),
            branch_code
        FROM staging_sales_060
        WHERE transaction_id != 'transaction_id' AND branch_code IS NOT NULL
    """)
    print("[OK] Ingestion complete. Physical branch partitions written to HDFS.\n")

    # 4. Execute the 4 Business Analytical Queries
    print("=" * 85)
    print("                    HIVEQL BUSINESS ANALYTICAL QUERIES                        ")
    print("=" * 85 + "\n")

    print("[QUERY 1] Branch-wise Sales Revenue & Contribution (%):")
    total_rev = spark.sql("SELECT SUM(total_amount) FROM sales_partitioned_060").collect()[0][0]
    q1 = f"""
        SELECT 
            branch_code,
            branch_city,
            COUNT(transaction_id) AS total_orders,
            ROUND(SUM(total_amount), 2) AS branch_revenue_inr,
            ROUND(AVG(total_amount), 2) AS avg_ticket_size_inr,
            ROUND(SUM(total_amount) * 100.0 / {total_rev}, 2) AS revenue_share_pct
        FROM sales_partitioned_060
        GROUP BY branch_code, branch_city
        ORDER BY branch_revenue_inr DESC
    """
    spark.sql(q1).show(truncate=False)

    print("[QUERY 2] Top 5 Best-Selling Products by Quantity Sold:")
    q2 = """
        SELECT 
            category,
            product_name,
            SUM(quantity) AS units_sold,
            ROUND(SUM(total_amount), 2) AS total_sales_inr
        FROM sales_partitioned_060
        GROUP BY category, product_name
        ORDER BY units_sold DESC
        LIMIT 5
    """
    spark.sql(q2).show(truncate=False)

    print("[QUERY 3] Peak Sales Hours (Hourly Transaction Density):")
    q3 = """
        SELECT 
            HOUR(transaction_timestamp) AS hour_of_day,
            COUNT(transaction_id) AS transaction_count,
            ROUND(SUM(total_amount), 2) AS hourly_revenue_inr
        FROM sales_partitioned_060
        GROUP BY HOUR(transaction_timestamp)
        ORDER BY transaction_count DESC
    """
    spark.sql(q3).show(10, truncate=False)

    print("[QUERY 4] Monthly Sales Turnover Trends (Jan - Apr 2026):")
    q4 = """
        SELECT 
            DATE_FORMAT(transaction_timestamp, 'yyyy-MM') AS sales_month,
            COUNT(transaction_id) AS total_transactions,
            SUM(quantity) AS total_items_sold,
            ROUND(SUM(total_amount), 2) AS gross_monthly_revenue_inr
        FROM sales_partitioned_060
        WHERE transaction_timestamp IS NOT NULL
        GROUP BY DATE_FORMAT(transaction_timestamp, 'yyyy-MM')
        ORDER BY sales_month ASC
    """
    spark.sql(q4).show(truncate=False)

    # 5. Proof of Physical HDFS Storage & Hive Partitions
    print("=" * 85)
    print("               PROOF OF REAL HDFS PARTITIONS & WAREHOUSE STORAGE              ")
    print("=" * 85)
    desc_df = spark.sql("DESCRIBE FORMATTED sales_partitioned_060")
    location_row = desc_df.filter(col("col_name") == "Location").collect()
    if location_row:
        print(f"[*] Hive Physical Table Location : {location_row[0]['data_type']}")

    print("\n[*] Querying real HDFS filesystem partitions via 'hdfs dfs -ls'...")
    try:
        res = subprocess.run(
            ["/usr/local/hadoop/bin/hdfs", "dfs", "-ls", f"/user/hive/warehouse/{DB_NAME.lower()}.db/sales_partitioned_060"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        print(res.stdout)
    except Exception as e:
        print(f"Error checking hdfs: {e}")

    spark.stop()
    print("[OK] Real Apache Hive / HDFS execution finished successfully!\n")

if __name__ == "__main__":
    main()
