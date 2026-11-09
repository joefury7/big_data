#!/bin/bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export SPARK_HOME=/home/joel/spark-env/lib/python3.12/site-packages/pyspark
METASTORE_PATH="/mnt/c/Users/JOEL/OneDrive/Desktop/big_data/metastore_db"

exec /home/joel/spark-env/bin/spark-sql \
  --conf "spark.hadoop.javax.jdo.option.ConnectionURL=jdbc:derby:;databaseName=$METASTORE_PATH;create=true" \
  --conf "spark.sql.warehouse.dir=hdfs://localhost:9000/user/hive/warehouse" \
  "$@"
