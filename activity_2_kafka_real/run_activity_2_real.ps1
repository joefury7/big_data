# ==============================================================================
#  ACTIVITY 2: REAL APACHE KAFKA RUNNER (POWERSHELL)
#  Student Name: Joel B John | USN: 1MS24CI060
# ==============================================================================

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  STARTING REAL APACHE KAFKA PROTOTYPE (USN: 1MS24CI060)" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

# 1. Start Kafka Broker Daemon in WSL if not running
Write-Host "[1/3] Ensuring Real Apache Kafka Broker is active on port 9092..." -ForegroundColor Yellow
wsl -d Ubuntu -u joel bash /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_2_kafka_real/start_real_kafka.sh

# 2. Run Producer to publish real events
Write-Host "[2/3] Launching Telemetry Producer (publishing 20 events)..." -ForegroundColor Yellow
wsl -d Ubuntu -u joel /home/joel/spark-env/bin/python /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_2_kafka_real/real_kafka_producer.py

# 3. Run Consumer to process events & show alerts
Write-Host "[3/3] Launching Consumer to process stream & generate alerts..." -ForegroundColor Green
wsl -d Ubuntu -u joel /home/joel/spark-env/bin/python -c "import sys; sys.path.append('/mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_2_kafka_real'); from real_kafka_consumer import run_real_consumer; run_real_consumer(max_messages=20)"

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "[SUCCESS] Real Apache Kafka execution complete!" -ForegroundColor Green
Write-Host "================================================================================" -ForegroundColor Cyan
