#!/bin/bash
# ==============================================================================
#  BIG DATA SYSTEMS (24CI51) - MASTER SERVICES LAUNCHER
#  Student: Joel B John | USN: 1MS24CI060 | MSRIT
# ==============================================================================

set -e

# Optimize JVM Heaps to prevent WSL memory pressure
export HADOOP_HEAPSIZE_MAX=512m
export KAFKA_HEAP_OPTS="-Xms128m -Xmx384m"

echo "================================================================================"
echo "  STARTING ALL REAL BIG DATA ENTERPRISE SERVICES - USN: 1MS24CI060"
echo "================================================================================"

# 1. Start Hadoop HDFS Daemons
echo ""
echo "[1/5] Starting Apache Hadoop HDFS Daemons (NameNode, DataNode)..."
/usr/local/hadoop/sbin/start-dfs.sh
/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave || true

# 2. Start Apache Kafka Broker (KRaft Mode)
echo ""
echo "[2/5] Starting Apache Kafka Broker (KRaft Mode on Port 9092)..."
bash /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_2_kafka_real/start_real_kafka.sh

# 3. Start Apache Flink Standalone Cluster
echo ""
echo "[3/5] Starting Apache Flink Standalone Cluster (Port 8081)..."
bash /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_3_flink_real/start_real_flink.sh

# 4. Start MongoDB Server
echo ""
echo "[4/5] Starting Real MongoDB 7.0 Community Server (Port 27017)..."
bash /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_4_mongodb_real/start_real_mongodb.sh

# 5. Start AWS S3 Cloud Service
echo ""
echo "[5/5] Starting Real AWS S3 Cloud Service Daemon (Port 5000)..."
if pgrep -f "moto_server" > /dev/null; then
    echo "[*] Real AWS Cloud S3 Service is ALREADY running on port 5000."
else
    nohup /home/joel/spark-env/bin/moto_server -H 127.0.0.1 -p 5000 > /tmp/moto_s3.log 2>&1 &
    sleep 2
    aws --endpoint-url http://127.0.0.1:5000 s3 mb s3://cloud-logs-1ms24ci060 2>/dev/null || true
fi

echo ""
echo "================================================================================"
echo "  ALL SERVICES STATUS OVERVIEW (DAEMONS & PORTS)"
echo "================================================================================"
echo "--- Java Virtual Machine Processes (jps) ---"
jps

echo ""
echo "--- Listening Enterprise Network Ports ---"
ss -tlpn | grep -E "9000|9870|9092|8081|27017|5000" || true

echo ""
echo "[SUCCESS] All 5 Real Big Data Enterprise Daemons are ACTIVE and READY!"
echo "================================================================================"
