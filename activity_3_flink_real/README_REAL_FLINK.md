# ACTIVITY 3 (PATH 2): REAL APACHE FLINK STREAM PROCESSING CLUSTER
**Course**: Big Data Systems (24CI51) - Self Learning Activity  
**Student Name**: Joel B John  
**USN**: 1MS24CI060  
**Department**: CSE (Artificial Intelligence & Machine Learning), MSRIT  

---

> **Educational & Synthetic Data Notice**: This prototype operates on synthetic patient telemetry and academic demonstration thresholds. The system is designed strictly for computational evaluation and must not be used as a clinical diagnostic tool.

---

## 1. What Makes This Implementation "Real"?
This implementation runs against a **genuine Apache Flink 1.18.1 JVM Cluster** paired with a live **Apache Kafka Broker**:
1. **Real Flink JobManager & TaskManager**: Operates a distributed stream execution cluster with worker task slots.
2. **Real Flink Web Dashboard**: Provides a real-time cluster monitor, metrics, task slot health, and job logs at:
   👉 **`http://localhost:8081`**
3. **Real Kafka Stream Ingestion**: Patient monitors emit telemetry to Kafka topic `patient_vitals_stream_1MS24CI060`, consumed by Flink in real time.
4. **Stateful 15-Second Tumbling Windows**: Aggregates mean heart rate, minimum oxygen saturation ($\text{SpO}_2$), and mean temperature per patient, flagging patients requiring clinical attention.

---

## 2. How to Run the Demo for Faculty

### Quick 1-Click Execution (from Windows PowerShell):
Inside `activity_3_flink_real/`, run:
```powershell
powershell -ExecutionPolicy Bypass -File run_activity_3_real.ps1
```

### Side-by-Side Terminals (To Impress Faculty):
* **Terminal 1 (Real Flink Stream Processor)**:
  ```bash
  wsl -d Ubuntu -u joel /home/joel/spark-env/bin/python /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_3_flink_real/real_flink_stream_job.py
  ```
* **Terminal 2 (Real IoT Medical Device Emitter)**:
  ```bash
  wsl -d Ubuntu -u joel /home/joel/spark-env/bin/python /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_3_flink_real/patient_vitals_kafka_producer.py
  ```

---

## 3. Indisputable Proof Commands for Faculty

### Proof 1: Flink Web Dashboard
Open your web browser and navigate to:
👉 **`http://localhost:8081`**
*Shows the official Apache Flink Web Console, live TaskManagers, available Task Slots, and JVM memory utilization.*

### Proof 2: Verify Flink JVM Processes via `jps`
```bash
wsl -d Ubuntu -u joel jps
```
**Output shows:**
```text
StandaloneSessionClusterEntrypoint   (JobManager)
TaskManagerRunner                   (TaskManager)
Kafka                               (Message Broker)
NameNode                            (Hadoop HDFS)
DataNode                            (Hadoop HDFS)
```

### Proof 3: Check Clinical Alert Log
```bash
cat /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_3_flink_real/real_flink_alerts_1MS24CI060.log
```
*Shows timestamped clinical breach alerts with vitals and doctor notification logs.*
