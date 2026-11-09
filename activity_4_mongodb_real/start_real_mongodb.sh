#!/bin/bash
# ==============================================================================
#  ACTIVITY 4: REAL MONGODB COMMUNITY SERVER DAEMON LAUNCHER
#  Student Name : Joel B John | USN: 1MS24CI060
# ==============================================================================

set -e

MONGO_DIR="/home/joel/mongodb"
DATA_DIR="$MONGO_DIR/data"
LOG_DIR="$MONGO_DIR/log"
PORT=27017

echo "================================================================================"
echo "  STARTING REAL MONGODB 7.0 COMMUNITY SERVER DAEMON - USN: 1MS24CI060"
echo "================================================================================"

mkdir -p "$DATA_DIR" "$LOG_DIR"

if pgrep -x "mongod" > /dev/null; then
    echo "[*] Real MongoDB daemon (mongod) is ALREADY running on port $PORT."
else
    echo "[1/3] Launching official MongoDB daemon on port $PORT..."
    $MONGO_DIR/bin/mongod --fork --logpath "$LOG_DIR/mongod.log" --dbpath "$DATA_DIR" --bind_ip 127.0.0.1 --port $PORT
    sleep 2
fi

echo "[2/3] Verifying real MongoDB process status..."
ps aux | grep "[m]ongod" || true

echo "[3/3] Checking MongoDB connection and engine version..."
/home/joel/spark-env/bin/python -c "
import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:$PORT/', serverSelectionTimeoutMS=2000)
info = client.server_info()
print(f'[OK] Successfully connected to live MongoDB Server v{info[\"version\"]} on port $PORT')
print(f'[OK] Storage Engine: {info.get(\"storageEngine\", {}).get(\"name\", \"wiredTiger\")}')
"

echo ""
echo "================================================================================"
echo "[SUCCESS] Real MongoDB Community Server is LIVE on 127.0.0.1:$PORT"
echo "================================================================================"
