# ==============================================================================
#  ACTIVITY 5: REAL AWS S3 CLOUD LOG ANALYTICS RUNNER (POWERSHELL)
#  Student Name: Joel B John | USN: 1MS24CI060
# ==============================================================================

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  EXECUTING ACTIVITY 5: REAL AWS S3 CLOUD LOG ANALYTICS (USN: 1MS24CI060)" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

# 1. Start Real AWS Cloud S3 Service Daemon
Write-Host "[1/2] Ensuring AWS Cloud S3 Service is active on port 5000 in WSL..." -ForegroundColor Yellow
wsl -d Ubuntu -u joel bash /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_5_cloud_real/start_real_cloud_s3.sh

# 2. Run Real Cloud Data Lake Pipeline
Write-Host "[2/2] Running Real Cloud Pipeline (S3 Parquet Ingestion, Glue Catalog & Athena SQL)..." -ForegroundColor Green
wsl -d Ubuntu -u joel /home/joel/spark-env/bin/python /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_5_cloud_real/real_cloud_log_pipeline.py

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "[SUCCESS] Real AWS S3 Cloud Analytics Pipeline Complete! Chart saved." -ForegroundColor Green
Write-Host "================================================================================" -ForegroundColor Cyan
