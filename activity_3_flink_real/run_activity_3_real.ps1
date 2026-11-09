# ==============================================================================
#  ACTIVITY 3: REAL APACHE FLINK STREAM PROCESSING RUNNER (POWERSHELL)
#  Student Name: Joel B John | USN: 1MS24CI060
# ==============================================================================

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  STARTING REAL APACHE FLINK MONITORING PIPELINE (USN: 1MS24CI060)" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

# 1. Start Flink Cluster & Kafka Broker
Write-Host "[1/3] Ensuring Kafka and Flink Clusters are active in WSL..." -ForegroundColor Yellow
wsl -d Ubuntu -u joel bash /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_3_flink_real/start_real_flink.sh

# 2. Launch Real Vitals Producer in background
Write-Host "[2/3] Launching Connected Medical Device Emitter (40 Events to Kafka)..." -ForegroundColor Yellow
Start-Process -FilePath "wsl.exe" -ArgumentList "-d", "Ubuntu", "-u", "joel", "/home/joel/spark-env/bin/python", "/mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_3_flink_real/patient_vitals_kafka_producer.py"

Start-Sleep -Seconds 2

# 3. Launch Real Flink Stream Processing Consumer
Write-Host "[3/3] Launching Real Flink Stream Processor (Point Anomaly + Tumbling Windows)..." -ForegroundColor Green
wsl -d Ubuntu -u joel /home/joel/spark-env/bin/python -c "import sys; sys.path.append('/mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_3_flink_real'); from real_flink_stream_job import run_real_flink_processor; run_real_flink_processor(max_events=40)"

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "[SUCCESS] Real Apache Flink stream processing execution complete!" -ForegroundColor Green
Write-Host "👉 Inspect real Flink cluster metrics at: http://localhost:8081" -ForegroundColor Yellow
Write-Host "================================================================================" -ForegroundColor Cyan
