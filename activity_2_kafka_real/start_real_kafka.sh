#!/bin/bash
# ==============================================================================
#  ACTIVITY 2: REAL APACHE KAFKA CLUSTER SETUP & LAUNCHER (KRAFT MODE)
#  Student Name : Joel B John | USN: 1MS24CI060
# ==============================================================================

set -e

KAFKA_DIR="/home/joel/kafka"
TOPIC_NAME="traffic_telemetry_1MS24CI060"
export KAFKA_HEAP_OPTS="-Xms128m -Xmx384m"

echo "================================================================================"
echo "  STARTING REAL APACHE KAFKA CLUSTER (KRAFT MODE) - USN: 1MS24CI060"
echo "================================================================================"

if [ ! -d "$KAFKA_DIR" ]; then
    echo "[!] Error: Kafka directory $KAFKA_DIR not found."
    exit 1
fi

# Check if Kafka is already running
if pgrep -f "kafka.Kafka" > /dev/null; then
    echo "[*] Real Apache Kafka broker is ALREADY running on port 9092."
else
    echo "[1/4] Checking KRaft storage formatting..."
    KRAFT_CONFIG="$KAFKA_DIR/config/kraft/server.properties"
    LOG_DIR="$KAFKA_DIR/data"

    if [ ! -f "$LOG_DIR/meta.properties" ]; then
        echo "[*] Generating new KRaft cluster ID..."
        CLUSTER_ID=$($KAFKA_DIR/bin/kafka-storage.sh random-uuid)
        echo "[*] Cluster ID: $CLUSTER_ID"
        echo "[*] Formatting Kafka log directories..."
        mkdir -p "$LOG_DIR"
        $KAFKA_DIR/bin/kafka-storage.sh format -t "$CLUSTER_ID" -c "$KRAFT_CONFIG"
    fi

    echo "[2/4] Starting Apache Kafka broker daemon on port 9092..."
    $KAFKA_DIR/bin/kafka-server-start.sh -daemon "$KRAFT_CONFIG"
    sleep 3
fi

echo "[3/4] Ensuring Kafka topic '$TOPIC_NAME' exists with 3 partitions..."
$KAFKA_DIR/bin/kafka-topics.sh --create --if-not-exists \
    --topic "$TOPIC_NAME" \
    --bootstrap-server localhost:9092 \
    --partitions 3 \
    --replication-factor 1

echo "[4/4] Verifying real Kafka topic metadata..."
$KAFKA_DIR/bin/kafka-topics.sh --describe \
    --topic "$TOPIC_NAME" \
    --bootstrap-server localhost:9092

echo ""
echo "================================================================================"
echo "[SUCCESS] Real Apache Kafka Broker is LIVE on localhost:9092"
echo "Topic '$TOPIC_NAME' is active with 3 partitions."
echo "================================================================================"
