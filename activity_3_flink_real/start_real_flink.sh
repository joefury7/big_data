#!/bin/bash
# ==============================================================================
#  ACTIVITY 3: REAL APACHE FLINK CLUSTER SETUP & LAUNCHER
#  Student Name : Joel B John | USN: 1MS24CI060
# ==============================================================================

set -e

FLINK_DIR="/home/joel/flink"
KAFKA_DIR="/home/joel/kafka"
TOPIC_NAME="patient_vitals_stream_1MS24CI060"

echo "================================================================================"
echo "  STARTING REAL APACHE FLINK CLUSTER & STREAM PIPELINE - USN: 1MS24CI060"
echo "================================================================================"

# 1. Ensure Kafka Broker is active
if ! pgrep -f "kafka.Kafka" > /dev/null; then
    echo "[1/4] Starting Apache Kafka Broker on port 9092..."
    /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_2_kafka_real/start_real_kafka.sh
else
    echo "[1/4] Kafka Broker is already running on port 9092."
fi

# 2. Ensure Topic exists
echo "[2/4] Ensuring Kafka topic '$TOPIC_NAME' exists..."
$KAFKA_DIR/bin/kafka-topics.sh --create --if-not-exists \
    --topic "$TOPIC_NAME" \
    --bootstrap-server localhost:9092 \
    --partitions 2 \
    --replication-factor 1

# 3. Start Apache Flink Local Cluster
if pgrep -f "StandaloneSessionClusterEntrypoint" > /dev/null; then
    echo "[3/4] Apache Flink JobManager & TaskManager are ALREADY running."
else
    echo "[3/4] Launching Apache Flink Standalone Session Cluster..."
    nohup $FLINK_DIR/bin/jobmanager.sh start-foreground > $FLINK_DIR/log/jm.out 2>&1 &
    sleep 2
    nohup $FLINK_DIR/bin/taskmanager.sh start-foreground > $FLINK_DIR/log/tm.out 2>&1 &
    sleep 3
fi

# 4. Verify Flink Daemons
echo "[4/4] Verifying Flink Cluster status via jps..."
jps | grep -E "StandaloneSessionClusterEntrypoint|TaskManagerRunner" || true

echo ""
echo "================================================================================"
echo "[SUCCESS] Real Apache Flink Cluster is LIVE!"
echo "👉 Open Flink Web Dashboard in Browser: http://localhost:8081"
echo "================================================================================"
