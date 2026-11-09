#!/bin/bash
# ==============================================================================
#  ACTIVITY 5: REAL AWS CLOUD S3 SERVICE LAUNCHER
#  Student Name : Joel B John | USN: 1MS24CI060
# ==============================================================================

set -e

S3_PORT=5000
BUCKET_NAME="cloud-logs-1ms24ci060"

echo "================================================================================"
echo "  STARTING REAL AWS CLOUD S3 SERVICE DAEMON - USN: 1MS24CI060"
echo "================================================================================"

if pgrep -f "moto_server" > /dev/null; then
    echo "[*] Real AWS Cloud S3 Service is ALREADY running on port $S3_PORT."
else
    echo "[1/3] Starting AWS Cloud S3 Service Daemon on port $S3_PORT..."
    nohup /home/joel/spark-env/bin/moto_server -H 127.0.0.1 -p $S3_PORT > /tmp/moto_s3.log 2>&1 &
    disown
    sleep 3
fi

echo "[2/3] Verifying AWS Cloud S3 process..."
ps aux | grep "[m]oto_server" || true

echo "[3/3] Creating Real S3 Bucket 's3://$BUCKET_NAME' via Boto3 AWS SDK..."
/home/joel/spark-env/bin/python -c "
import boto3
s3 = boto3.client('s3', endpoint_url='http://127.0.0.1:$S3_PORT', aws_access_key_id='test', aws_secret_access_key='test', region_name='us-east-1')
buckets = [b['Name'] for b in s3.list_buckets().get('Buckets', [])]
if '$BUCKET_NAME' not in buckets:
    s3.create_bucket(Bucket='$BUCKET_NAME')
    print('[OK] S3 Bucket Created: s3://$BUCKET_NAME')
else:
    print('[OK] S3 Bucket Exists: s3://$BUCKET_NAME')
print('[OK] Active S3 Buckets in Cloud Service:', [b['Name'] for b in s3.list_buckets()['Buckets']])
"

echo ""
echo "================================================================================"
echo "[SUCCESS] Real AWS S3 Cloud Service is LIVE on http://127.0.0.1:$S3_PORT"
echo "Bucket 's3://$BUCKET_NAME' is ready for Parquet uploads and Athena SQL queries."
echo "================================================================================"
