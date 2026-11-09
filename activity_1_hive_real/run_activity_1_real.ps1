# ==============================================================================
#  ACTIVITY 1: REAL APACHE HIVE ON HDFS RUNNER (POWERSHELL)
#  Student Name: Joel B John | USN: 1MS24CI060
# ==============================================================================

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  STARTING REAL APACHE HIVE ON HDFS (USN: 1MS24CI060)" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

# 1. Ensure HDFS is running
Write-Host "[1/3] Ensuring Hadoop NameNode and DataNode are live in WSL..." -ForegroundColor Yellow
wsl -d Ubuntu -u joel /usr/local/hadoop/sbin/start-dfs.sh
wsl -d Ubuntu -u joel /usr/local/hadoop/bin/hdfs dfsadmin -safemode leave

# 2. Upload dataset to HDFS if not exists
Write-Host "[2/3] Uploading Sales Dataset to HDFS path /user/joel/retail_warehouse_1MS24CI060/raw_sales..." -ForegroundColor Yellow
wsl -d Ubuntu -u joel bash -c "/usr/local/hadoop/bin/hdfs dfs -mkdir -p /user/joel/retail_warehouse_1MS24CI060/raw_sales && /usr/local/hadoop/bin/hdfs dfs -put -f /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_1_hive_real/sales_data_1MS24CI060.csv /user/joel/retail_warehouse_1MS24CI060/raw_sales/"

# 3. Execute Real Hive / Spark SQL Warehouse Job
Write-Host "[3/3] Executing HiveQL Analytics Job over HDFS..." -ForegroundColor Green
wsl -d Ubuntu -u joel /home/joel/spark-env/bin/python /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_1_hive_real/real_hive_job.py

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "[SUCCESS] Real Apache Hive on HDFS execution complete!" -ForegroundColor Green
Write-Host "================================================================================" -ForegroundColor Cyan
