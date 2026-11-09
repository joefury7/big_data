# ACTIVITY 1 (PATH 2): REAL APACHE HIVE ON HADOOP HDFS
**Course**: Big Data Systems (24CI51) - Self Learning Activity  
**Student Name**: Joel B John  
**USN**: 1MS24CI060  
**Department**: CSE (Artificial Intelligence & Machine Learning), MSRIT  

---

## 1. What Makes This Implementation "Real"?
Unlike a pure python calculation script, this implementation executes against a **real distributed Hadoop cluster and Apache Hive Metastore**:
1. **Real HDFS Storage**: The transactional dataset (`sales_data_1MS24CI060.csv`) is uploaded directly into Hadoop Distributed File System at:
   `hdfs://localhost:9000/user/joel/retail_warehouse_1MS24CI060/raw_sales/`
2. **Real Hive Metastore (HMS)**: Spark SQL initializes the genuine Apache Hive Metastore, cataloging database `hive_retail_1MS24CI060`.
3. **Real HDFS Partitions**: The production table `sales_partitioned_060` is physically split into discrete HDFS directories partitioned by `branch_code` in ORC format at:
   `hdfs://localhost:9000/user/hive/warehouse/hive_retail_1ms24ci060.db/sales_partitioned_060/`

---

## 2. Prerequisites & Architecture
- **Hadoop Version**: Apache Hadoop 3.3.6 (Running NameNode, DataNode, SecondaryNameNode).
- **Execution Engine**: Spark SQL with Hive Metastore support (`enableHiveSupport()`).
- **Storage Subsystem**: HDFS NameNode RPC port `9000`, Web UI port `9870`.

---

## 3. How to Run the Live Demo for Faculty

### Quick 1-Command Execution (from Windows PowerShell):
Inside `activity_1_hive_real/`, run:
```powershell
powershell -ExecutionPolicy Bypass -File run_activity_1_real.ps1
```
*(Or directly from workspace root: `powershell -ExecutionPolicy Bypass -File activity_1_hive_real/run_activity_1_real.ps1`)*

---

## 4. Indisputable Proof Commands to Show the Faculty

### Proof 1: NameNode Web UI
Open your web browser and go to:
👉 **`http://localhost:9870`**
*Shows the official Apache Hadoop NameNode Web Console, live DataNodes, storage capacity, and block replication.*

### Proof 2: Inspect Real Partitions in HDFS
Run in terminal:
```bash
wsl -d Ubuntu -u joel /usr/local/hadoop/bin/hdfs dfs -ls /user/hive/warehouse/hive_retail_1ms24ci060.db/sales_partitioned_060
```
**Expected Output:**
```text
drwxr-xr-x   - joel supergroup   /user/hive/warehouse/hive_retail_1ms24ci060.db/sales_partitioned_060/branch_code=JBJ_BLR_INDIRA_060
drwxr-xr-x   - joel supergroup   /user/hive/warehouse/hive_retail_1ms24ci060.db/sales_partitioned_060/branch_code=JBJ_BLR_MSRIT_060
drwxr-xr-x   - joel supergroup   /user/hive/warehouse/hive_retail_1ms24ci060.db/sales_partitioned_060/branch_code=JBJ_CHN_TNAGAR_060
drwxr-xr-x   - joel supergroup   /user/hive/warehouse/hive_retail_1ms24ci060.db/sales_partitioned_060/branch_code=JBJ_DEL_CP_060
drwxr-xr-x   - joel supergroup   /user/hive/warehouse/hive_retail_1ms24ci060.db/sales_partitioned_060/branch_code=JBJ_MUM_BANDRA_060
```

### Proof 3: Check JVM Daemons via `jps`
```bash
wsl -d Ubuntu -u joel jps
```
*Shows `NameNode`, `DataNode`, and `SecondaryNameNode` active.*
