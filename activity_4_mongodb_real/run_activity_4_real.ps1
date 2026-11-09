# ==============================================================================
#  ACTIVITY 4: REAL MONGODB SERVER RUNNER (POWERSHELL)
#  Student Name: Joel B John | USN: 1MS24CI060
# ==============================================================================

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  EXECUTING ACTIVITY 4: REAL MONGODB 7.0 COMMUNITY SERVER (USN: 1MS24CI060)" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

# 1. Ensure real mongod daemon is running on port 27017
Write-Host "[1/2] Ensuring MongoDB Daemon (mongod) is live on port 27017 in WSL..." -ForegroundColor Yellow
wsl -d Ubuntu -u joel bash /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_4_mongodb_real/start_real_mongodb.sh

# 2. Run real PyMongo job with explain plans
Write-Host "[2/2] Executing Real MongoDB Job (CRUD, Aggregations, COLLSCAN vs IXSCAN)..." -ForegroundColor Green
wsl -d Ubuntu -u joel /home/joel/spark-env/bin/python /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_4_mongodb_real/real_mongodb_catalog_job.py

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "[SUCCESS] Real MongoDB 7.0 execution complete!" -ForegroundColor Green
Write-Host "================================================================================" -ForegroundColor Cyan
