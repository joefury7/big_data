# Big Data Systems (24CI51) — Production Enterprise Implementations

**Student Name:** Joel B John  
**USN:** `1MS24CI060`  
**Department:** Computer Science & Engineering (Artificial Intelligence & Machine Learning)  
**Institution:** Ramaiah Institute of Technology (MSRIT), Bengaluru  
**Course Code:** 24CI51 (Big Data Systems) — Self-Learning Activities (SLAs 1 to 5)  
**Implementation Mode:** Path 2 — Real Enterprise Production Engines (Zero Mocking / No Simulations)  

---

## 📋 Repository Overview

This repository contains the complete, production-grade implementations of all five Self-Learning Activities (SLAs) for the **Big Data Systems (24CI51)** curriculum. Every activity runs on live enterprise daemons within an Ubuntu Linux subsystem (WSL2), accompanied by automated service orchestration, end-to-end telemetry pipelines, verification scripts, and 43 empirical screenshot proofs.

```
big_data/
├── activity_1_hive_real/        # Activity 1: Hadoop HDFS & Apache Spark-SQL Warehouse
├── activity_2_kafka_real/       # Activity 2: Apache Kafka (KRaft Mode) Streaming Pipeline
├── activity_3_flink_real/       # Activity 3: Apache Flink Real-Time Patient Stream Processing
├── activity_4_mongodb_real/     # Activity 4: MongoDB 7.0 WiredTiger Polymorphic Catalog
├── activity_5_cloud_real/       # Activity 5: Serverless Cloud AWS S3 + Athena Parquet Analytics
├── final_report/                # Consolidated 20-Mark Reports (DOCX & Markdown)
├── ss/                          # 43 High-Resolution Terminal & Dashboard Screenshots
├── start_all_services.sh        # Master Multi-Daemon Orchestration Script
├── TERMINAL_SCREENSHOT_RUNBOOK_1MS24CI060.md # Step-by-Step Command Runbook
└── README.md
```

---

## 🛠️ Technology Stack & Architectures

| Activity | Big Data Paradigm | Real Platform / Daemon | Storage / Data Engine | Primary Use Case |
| :---: | :--- | :--- | :--- | :--- |
| **Activity 1** | Distributed Batch / OLAP | Apache Hadoop HDFS + Apache Spark-SQL | HDFS Block Storage + Hive Metastore | Retail Data Warehouse & Revenue Aggregation |
| **Activity 2** | Event Streaming Backbone | Apache Kafka (KRaft Mode, Port 9092) | Multi-Partition Commit Log (Murmur2 Keys) | Smart City Traffic Telemetry & Congestion Alerts |
| **Activity 3** | True Event-Driven Streaming | Apache Flink 1.18.1 (JobManager Port 8081) | DataStream API + 15s Tumbling Windows | Real-Time ICU Patient Biometric Monitoring |
| **Activity 4** | Document NoSQL / OLTP | MongoDB 7.0 Community (Port 27017) | WiredTiger Engine + Compound B-Tree Indexes | Polymorphic E-Commerce SKU Catalog Analytics |
| **Activity 5** | Serverless Cloud Lakehouse | AWS S3 REST API (Port 5000) + Amazon Athena | Snappy Apache Parquet + AWS Glue Catalog | HTTP Access Log Observability & SLA Audits |

---

## 🚀 Quick Start: Running the Services

All enterprise services can be orchestrated with a single master command from WSL2 / Ubuntu:

```bash
# 1. Start all 5 background enterprise daemons
/mnt/c/Users/JOEL/OneDrive/Desktop/big_data/start_all_services.sh

# 2. Verify all JVM daemons running
jps
# Output shows: NameNode, DataNode, SecondaryNameNode, Kafka, TaskManagerRunner, StandaloneSessionClusterEntrypoint

# 3. Verify enterprise listener ports
ss -tlpn | grep -E "9000|9870|9092|8081|27017|5000"
```

---

## 📂 Detailed Activity Breakdown

### Activity 1: Retail Data Warehouse (Hadoop HDFS + Spark-SQL)
- **Directory:** `activity_1_hive_real/`
- **Data Ingestion:** Ingested 6,000 retail transactions into HDFS distributed namespace under `/user/joel/retail_warehouse_1MS24CI060/raw_sales/`.
- **Partitioning Strategy:** Managed Hive warehouse table `sales_partitioned_060` partitioned physically by `branch_code` across 5 metropolitan branches (Indira Nagar, MSRIT Campus, Bandra West, T. Nagar, Connaught Place).
- **Execution:** Spark Catalyst Optimizer pushes predicates directly to HDFS file scan level, skipping 80% of unreferenced branch directories and aggregating revenue in **2.946 seconds**.

### Activity 2: Smart City Traffic Telemetry (Apache Kafka KRaft)
- **Directory:** `activity_2_kafka_real/`
- **Cluster Architecture:** Apache Kafka running in KRaft mode (no ZooKeeper dependency) with 3 horizontal topic partitions.
- **Key Hashing:** Producer hashes `sensor_id` via Murmur2 algorithm, guaranteeing deterministic FIFO ordering per junction.
- **Alerting Engine:** Consumer group `traffic_monitoring_group_1MS24CI060` intercepts severe congestion incidents (<15 km/h, >60 vehicles) within **6.2 milliseconds** with **zero consumer lag**.

### Activity 3: Healthcare Patient Telemetry (Apache Flink Streaming)
- **Directory:** `activity_3_flink_real/`
- **Streaming Pipeline:** Ingests non-stop biometric streams (Heart Rate, SpO2 %, Temperature) from Kafka.
- **Event-Driven Alerts:** Sub-millisecond detection of physiological breaches: Tachycardia (>110 bpm), Bradycardia (<50 bpm), and Hypoxemia Desaturation (<92%).
- **Web Dashboard:** Live cluster monitoring at `http://localhost:8081` with distributed DAG execution, stateful tumbling windows, and **0% backpressure**.

### Activity 4: Polymorphic E-Commerce Catalog (MongoDB 7.0 WiredTiger)
- **Directory:** `activity_4_mongodb_real/`
- **Document Store:** Database `real_store_1MS24CI060` housing 5,007 polymorphic product documents across 5 merchandise categories.
- **Schema Flexibility:** Complex hardware specs (Intel i7, 16GB RAM, OLED) and food attributes (Chikmagalur coffee origin, FSSAI) seamlessly coexist.
- **Execution Plan Proof:** `explain("executionStats")` confirms winning stage `FETCH` over `IXSCAN` using compound B-Tree index `category_1_price_1`, examining exactly 805 keys for 805 docs in **5 ms** (vs 5,007-doc `COLLSCAN`).

### Activity 5: Serverless Cloud Log Analytics (AWS S3 + Athena + Parquet)
- **Directory:** `activity_5_cloud_real/`
- **Columnar Compression:** Transformed 10,000 raw HTTP access logs from CSV (933 KB) into Snappy Parquet (311 KB), achieving **66.7% storage reduction**.
- **Serverless SQL:** Amazon Athena queries S3 Parquet partitions directly via AWS Glue catalog schema, analyzing 4xx/5xx error frequencies, peak traffic surges, and SLA compliance.
- **Cost Model:** Empirical AWS pricing model reveals **74.5% monthly savings** ($105.55/mo serverless vs $415.00/mo traditional 24/7 EMR clusters).

---

## 📊 Consolidated Laboratory Report

A comprehensive academic report conforming to the 20-mark evaluation rubric of the Department of CSE (AI & ML) is available in `final_report/`:

- **Microsoft Word Report:** [`final_report/FINAL_BIG_DATA_REPORT_1MS24CI060.docx`](final_report/FINAL_BIG_DATA_REPORT_1MS24CI060.docx) *(Contains all 43 embedded screenshot proofs)*
- **Markdown Draft Report:** [`final_report/DRAFT_REPORT_1MS24CI060_WITH_SCREENSHOTS.md`](final_report/DRAFT_REPORT_1MS24CI060_WITH_SCREENSHOTS.md)
- **Step-by-Step Screenshot Runbook:** [`TERMINAL_SCREENSHOT_RUNBOOK_1MS24CI060.md`](TERMINAL_SCREENSHOT_RUNBOOK_1MS24CI060.md)

---

## 👤 Author
**Joel B John**  
USN: `1MS24CI060`  
Department of CSE (Artificial Intelligence & Machine Learning)  
Ramaiah Institute of Technology, Bengaluru - 560054  
GitHub: [@joefury7](https://github.com/joefury7)
