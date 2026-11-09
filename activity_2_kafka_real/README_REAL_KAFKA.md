# ACTIVITY 2 (PATH 2): REAL APACHE KAFKA CLUSTER & ALERT ENGINE
**Course**: Big Data Systems (24CI51) - Self Learning Activity  
**Student Name**: Joel B John  
**USN**: 1MS24CI060  
**Department**: CSE (Artificial Intelligence & Machine Learning), MSRIT  

---

## 1. What Makes This Implementation "Real"?
This implementation runs against a **genuine Apache Kafka 3.7.0 JVM Broker** executing on `localhost:9092`:
1. **KRaft Mode (Kafka Raft Metadata)**: Uses modern KRaft quorum protocol rather than legacy ZooKeeper.
2. **Real Kafka Topic**: `traffic_telemetry_1MS24CI060` created with **3 partitions** on disk.
3. **Partitioned Routing**: The Python producer hashes the `sensor_id` key so telemetry from each junction is mapped to a dedicated partition.
4. **Committed Consumer Offsets**: Offsets are persisted to Kafka's internal `__consumer_offsets` topic.

---

## 2. How to Run the Demo for Faculty

### Quick 1-Click Execution (from Windows PowerShell):
Inside `activity_2_kafka_real/`, run:
```powershell
powershell -ExecutionPolicy Bypass -File run_activity_2_real.ps1
```

### Side-by-Side Terminals (To Impress Faculty):
* **Terminal 1 (Real Consumer)**:
  ```bash
  wsl -d Ubuntu -u joel /home/joel/spark-env/bin/python /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_2_kafka_real/real_kafka_consumer.py
  ```
* **Terminal 2 (Real Producer)**:
  ```bash
  wsl -d Ubuntu -u joel /home/joel/spark-env/bin/python /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_2_kafka_real/real_kafka_producer.py
  ```

---

## 3. Indisputable Proof Commands for Faculty

### Proof 1: Verify Kafka JVM Process via `jps`
```bash
wsl -d Ubuntu -u joel jps
```
**Output shows:**
```text
3833 Kafka
624 NameNode
803 DataNode
```

### Proof 2: Describe Real Topic Partitions
```bash
wsl -d Ubuntu -u joel /home/joel/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic traffic_telemetry_1MS24CI060
```
**Output:**
```text
Topic: traffic_telemetry_1MS24CI060  PartitionCount: 3  ReplicationFactor: 1
    Partition: 0  Leader: 1  Replicas: 1  Isr: 1
    Partition: 1  Leader: 1  Replicas: 1  Isr: 1
    Partition: 2  Leader: 1  Replicas: 1  Isr: 1
```

### Proof 3: Verify Consumer Offsets & Lag
```bash
wsl -d Ubuntu -u joel /home/joel/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group traffic_monitoring_group_1MS24CI060
```
**Output:**
```text
GROUP                               TOPIC                        PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
traffic_monitoring_group_1MS24CI060 traffic_telemetry_1MS24CI060 0          9               9               0
traffic_monitoring_group_1MS24CI060 traffic_telemetry_1MS24CI060 1          17              17              0
traffic_monitoring_group_1MS24CI060 traffic_telemetry_1MS24CI060 2          4               4               0
```
*(Total offsets = 30 events with 0 lag).*
