# Activity 4 (Path 2): Real MongoDB 7.0 Community Server

**Student Name**: Joel B John  
**USN**: 1MS24CI060  
**Department**: Computer Science & Engineering (Artificial Intelligence & Machine Learning)  
**Institution**: Ramaiah Institute of Technology (MSRIT), Bengaluru  
**Course Code**: 24CI51 (Big Data Systems)  

---

## 1. Real Technology Architecture
Unlike simulations, this directory runs against the **official MongoDB 7.0 Community Server daemon (`mongod`)** using the high-performance **WiredTiger storage engine** on port `27017` in Ubuntu WSL2.

- **MongoDB Version**: `7.0.14`
- **Host / Port**: `127.0.0.1:27017`
- **Database Name**: `real_store_1MS24CI060`
- **Collection Name**: `products_catalog_060`
- **Storage Engine**: `wiredTiger` with document-level concurrency and Snappy block compression.

---

## 2. Execution Instructions

### One-Click Execution (from Windows PowerShell)
```powershell
cd C:\Users\JOEL\OneDrive\Desktop\big_data
.\activity_4_mongodb_real\run_activity_4_real.ps1
```

### Manual WSL Terminal Commands
```bash
# 1. Start real MongoDB daemon
/home/joel/mongodb/bin/mongod --fork --logpath /home/joel/mongodb/log/mongod.log --dbpath /home/joel/mongodb/data --bind_ip 127.0.0.1 --port 27017

# 2. Check running process
ps aux | grep mongod

# 3. Run real catalog script
/home/joel/spark-env/bin/python /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_4_mongodb_real/real_mongodb_catalog_job.py
```

---

## 3. Real Empirical Evidence from MongoDB Engine

### Verification of Live Process
```
joel       12549  6.3  0.9 541396 116012 ?       Sl   15:22   0:00 /home/joel/mongodb/bin/mongod --fork --logpath /home/joel/mongodb/log/mongod.log --dbpath /home/joel/mongodb/data --bind_ip 127.0.0.1
```

### Real Execution Plan Comparison (`explain("executionStats")`)
- **Before Compound Index**:
  - Stage: `COLLSCAN` (Full Collection Scan)
  - Total Documents Examined: `5,007`
  - Scanned every document in the database sequentially.
- **After Compound Index (`category_1_price_1`)**:
  - Stage: `FETCH -> IXSCAN` (B-Tree Index Traverse)
  - Index Name Used: `category_1_price_1`
  - Total Documents Examined: Only matching subset (~180 documents).
  - **Document Scan Reduction: >96% I/O saved on disk!**
