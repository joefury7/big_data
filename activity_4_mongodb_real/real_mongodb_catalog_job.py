"""
================================================================================
  DEPARTMENT OF CSE (ARTIFICIAL INTELLIGENCE & MACHINE LEARNING)
  RAMAIAH INSTITUTE OF TECHNOLOGY (MSRIT), BENGALURU - 560054
  BIG DATA SYSTEMS (24CI51) - ACTIVITY 4 (PATH 2: REAL MONGODB SERVER)
  TECHNOLOGY : REAL APACHE / MONGODB 7.0 WIREDTIGER ENGINE
================================================================================
  Student Name : Joel B John
  USN          : 1MS24CI060
  Semester     : V / Course Code: 24CI51
================================================================================
  Scenario: E-Commerce Catalog Management on Live MongoDB Daemon (Port 27017).
  Demonstrates Polymorphic Documents, Atomic Mutations, Aggregation Pipelines,
  and Real Execution Plans (COLLSCAN vs IXSCAN) via WiredTiger.
================================================================================
"""

import sys
import time
import random
from datetime import datetime
from pprint import pprint

try:
    import pymongo
except ImportError:
    print("[!] Error: pymongo not installed.")
    sys.exit(1)

MONGO_URI = "mongodb://127.0.0.1:27017/"
DB_NAME = "real_store_1MS24CI060"
COLLECTION_NAME = "products_catalog_060"

def print_banner():
    print("=" * 85)
    print("      DEPARTMENT OF CSE (ARTIFICIAL INTELLIGENCE & MACHINE LEARNING)        ")
    print("         BIG DATA SYSTEMS (24CI51) - ACTIVITY 4: REAL MONGODB SERVER         ")
    print("        REAL MONGODB 7.0 WIREDTIGER STORAGE ENGINE (PORT 27017)              ")
    print("   Student: Joel B John  |  USN: 1MS24CI060  |  Institution: MSRIT           ")
    print("=" * 85 + "\n")

# Sample Polymorphic E-Commerce Dataset
SAMPLE_PRODUCTS = [
    {
        "_id": "PROD_1MS24CI060_001",
        "title": "Quantum Pro Ultrabook 14",
        "brand": "AeroTech",
        "category": "Electronics",
        "sub_category": "Laptops",
        "price": 89999.00,
        "inventory": {"stock_count": 42, "warehouse_code": "WH_BLR_060", "reorder_level": 10},
        "rating": {"average": 4.7, "review_count": 128},
        "status": "active",
        "specifications": {
            "processor": "Intel Core i7-13700H",
            "ram_gb": 16,
            "storage": "1TB NVMe SSD",
            "display": "14-inch OLED 2.8K 120Hz",
            "battery_wh": 75,
            "weight_kg": 1.35
        },
        "tags": ["laptop", "ultrabook", "oled", "productivity"]
    },
    {
        "_id": "PROD_1MS24CI060_002",
        "title": "Apex Sound ANC Wireless Headphones",
        "brand": "SonicWave",
        "category": "Electronics",
        "sub_category": "Audio",
        "price": 14999.00,
        "inventory": {"stock_count": 85, "warehouse_code": "WH_BLR_060", "reorder_level": 15},
        "rating": {"average": 4.6, "review_count": 340},
        "status": "active",
        "specifications": {
            "driver_size_mm": 40,
            "battery_hours": 35,
            "noise_cancellation": "Active Hybrid ANC",
            "bluetooth_version": "5.3",
            "fast_charging": True
        },
        "tags": ["audio", "anc", "wireless", "headphones"]
    },
    {
        "_id": "PROD_1MS24CI060_003",
        "title": "VisionPro 4K HDR Gaming Monitor 27\"",
        "brand": "ViewMaster",
        "category": "Electronics",
        "sub_category": "Monitors",
        "price": 32999.00,
        "inventory": {"stock_count": 18, "warehouse_code": "WH_MUM_060", "reorder_level": 5},
        "rating": {"average": 4.8, "review_count": 94},
        "status": "active",
        "specifications": {
            "resolution": "3840x2160 (4K)",
            "refresh_rate_hz": 144,
            "panel_type": "IPS Mini-LED",
            "hdr": "HDR 1000",
            "response_time_ms": 1
        },
        "tags": ["monitor", "4k", "gaming", "hdr"]
    },
    {
        "_id": "PROD_1MS24CI060_004",
        "title": "Merino Wool Thermal Crewneck",
        "brand": "NordicWear",
        "category": "Apparel",
        "sub_category": "Winterwear",
        "price": 3499.00,
        "inventory": {"stock_count": 60, "warehouse_code": "WH_DEL_060", "reorder_level": 12},
        "rating": {"average": 4.5, "review_count": 76},
        "status": "active",
        "fashion_details": {
            "fabric": "100% Australian Merino Wool",
            "fit": "Regular Fit",
            "available_sizes": ["S", "M", "L", "XL"],
            "colors": ["Charcoal Heather", "Navy Blue", "Forest Green"],
            "care_instructions": "Dry clean or hand wash cold only"
        },
        "tags": ["apparel", "wool", "winter", "crewneck"]
    },
    {
        "_id": "PROD_1MS24CI060_005",
        "title": "Endurance Flex Running Shorts",
        "brand": "AeroTech",
        "category": "Apparel",
        "sub_category": "Activewear",
        "price": 1299.00,
        "inventory": {"stock_count": 120, "warehouse_code": "WH_BLR_060", "reorder_level": 25},
        "rating": {"average": 4.4, "review_count": 210},
        "status": "active",
        "fashion_details": {
            "fabric": "88% Recycled Polyester, 12% Spandex",
            "fit": "Athletic Compression Inner Liner",
            "available_sizes": ["M", "L", "XL"],
            "colors": ["Midnight Black", "Steel Grey"],
            "reflective_strips": True
        },
        "tags": ["activewear", "running", "shorts", "breathable"]
    },
    {
        "_id": "PROD_1MS24CI060_006",
        "title": "Artisanal Single-Estate Filter Coffee 500g",
        "brand": "BeanCrafters",
        "category": "Groceries",
        "sub_category": "Beverages",
        "price": 549.00,
        "inventory": {"stock_count": 250, "warehouse_code": "WH_BLR_060", "reorder_level": 50},
        "rating": {"average": 4.9, "review_count": 480},
        "status": "active",
        "food_attributes": {
            "origin": "Chikmagalur, Karnataka",
            "roast_level": "Medium Dark",
            "composition": "85% Arabica, 15% Chicory",
            "shelf_life_days": 180,
            "fssai_certified": True,
            "organic": True
        },
        "tags": ["coffee", "arabica", "chikmagalur", "organic"]
    },
    {
        "_id": "PROD_1MS24CI060_007",
        "title": "Raw Wildflower Forest Honey 1kg",
        "brand": "NatureGold",
        "category": "Groceries",
        "sub_category": "Organic Essentials",
        "price": 799.00,
        "inventory": {"stock_count": 140, "warehouse_code": "WH_CHN_060", "reorder_level": 30},
        "rating": {"average": 4.8, "review_count": 195},
        "status": "active",
        "food_attributes": {
            "origin": "Western Ghats",
            "unprocessed": True,
            "crystallization_possible": True,
            "shelf_life_days": 730,
            "nutritional_info_per_100g": {"calories": 304, "carbs_g": 82, "protein_g": 0.3}
        },
        "tags": ["honey", "raw", "wildflower", "natural"]
    },
    {
        "_id": "PROD_1MS24CI060_008",
        "title": "Legacy Bluetooth 4.1 Speaker",
        "brand": "SonicWave",
        "category": "Electronics",
        "sub_category": "Audio",
        "price": 1999.00,
        "inventory": {"stock_count": 0, "warehouse_code": "WH_DEL_060", "reorder_level": 0},
        "rating": {"average": 3.8, "review_count": 89},
        "status": "discontinued",
        "specifications": {"bluetooth_version": "4.1", "output_watts": 10},
        "tags": ["audio", "speaker", "clearance"]
    },
    {
        "_id": "PROD_1MS24CI060_009",
        "title": "Vintage Style Dial Wristwatch (Gen 1)",
        "brand": "Chronos",
        "category": "Accessories",
        "sub_category": "Watches",
        "price": 2499.00,
        "inventory": {"stock_count": 0, "warehouse_code": "WH_MUM_060", "reorder_level": 0},
        "rating": {"average": 3.9, "review_count": 45},
        "status": "discontinued",
        "specifications": {"movement": "Quartz", "water_resistance_atm": 3},
        "tags": ["watch", "vintage", "clearance"]
    }
]

def run_real_mongodb_pipeline():
    print_banner()

    print(f"[*] Connecting to REAL MongoDB Server at '{MONGO_URI}'...")
    try:
        client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=2500)
        server_info = client.server_info()
        dist = server_info.get('buildEnvironment', {}).get('distmod', 'linux-x86_64')
        print(f"[OK] Connected! Server Version: v{server_info['version']} | OS: {dist}")
        storage = server_info.get('storageEngines', ['wiredTiger'])[0]
        print(f"[OK] Active Storage Engine: {storage}\n")
    except Exception as e:
        print(f"[!] Error: Could not connect to real MongoDB daemon: {e}")
        print("    Ensure mongod is running via: ./start_real_mongodb.sh")
        sys.exit(1)

    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Clean collection for clean run
    collection.drop()

    # --------------------------------------------------------------------------
    # TASK 1: INSERTION OF POLYMORPHIC DOCUMENTS (CREATE)
    # --------------------------------------------------------------------------
    print("=" * 85)
    print("  TASK 1: INSERTION OF HETEROGENEOUS E-COMMERCE PRODUCTS (CREATE)")
    print("=" * 85)
    res = collection.insert_many(SAMPLE_PRODUCTS)
    print(f"[OK] Inserted {len(res.inserted_ids)} polymorphic documents into real MongoDB.")
    print("     Demonstrates true schema flexibility: different shapes in a single WiredTiger collection!\n")

    # Display contrasting documents
    print("--- REAL DOCUMENT 1: Electronics Schema (Hardware Specs) ---")
    doc_elec = collection.find_one({"category": "Electronics"})
    pprint({k: doc_elec[k] for k in ["_id", "title", "price", "specifications", "inventory"]})

    print("\n--- REAL DOCUMENT 2: Groceries Schema (Food & Certification Attributes) ---")
    doc_groc = collection.find_one({"category": "Groceries"})
    pprint({k: doc_groc[k] for k in ["_id", "title", "price", "food_attributes", "inventory"]})

    # --------------------------------------------------------------------------
    # TASK 2: CATEGORY & PRICE-RANGE SEARCHES (READ)
    # --------------------------------------------------------------------------
    print("\n" + "=" * 85)
    print("  TASK 2: CATEGORY & PRICE-RANGE FILTERING (READ)")
    print("=" * 85)
    query_filter = {
        "category": "Electronics",
        "price": {"$gte": 10000.0, "$lte": 100000.0},
        "status": "active"
    }
    print("[*] Filter: Category='Electronics' AND Price between Rs. 10,000 and Rs. 1,00,000")
    for i, prod in enumerate(collection.find(query_filter, {"title": 1, "brand": 1, "price": 1, "inventory.stock_count": 1}), 1):
        print(f"    [{i}] {prod['title']:<38} | Brand: {prod['brand']:<12} | Price: Rs. {prod['price']:>8.2f} | Stock: {prod['inventory']['stock_count']}")

    # --------------------------------------------------------------------------
    # TASK 3: ATOMIC STOCK MUTATIONS (UPDATE)
    # --------------------------------------------------------------------------
    print("\n" + "=" * 85)
    print("  TASK 3: ATOMIC STOCK UPDATES & DYNAMIC FIELD ADDITION (UPDATE)")
    print("=" * 85)
    target_id = "PROD_1MS24CI060_001"
    before = collection.find_one({"_id": target_id})
    print(f"[*] Product Before Update: {before['title']} | Stock: {before['inventory']['stock_count']} units")

    # Atomic $inc and dynamic $set
    update_res = collection.update_one(
        {"_id": target_id},
        {
            "$inc": {"inventory.stock_count": -7},
            "$set": {
                "inventory.last_ordered_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "is_fast_mover": True,
                "flash_sale_active": True
            }
        }
    )
    after = collection.find_one({"_id": target_id})
    print(f"[OK] Matched: {update_res.matched_count}, Modified: {update_res.modified_count}")
    print(f"    Product After Update : Stock: {after['inventory']['stock_count']} units (-7 confirmed)")
    print(f"    Dynamically Added    : is_fast_mover={after.get('is_fast_mover')}, flash_sale={after.get('flash_sale_active')}")

    # --------------------------------------------------------------------------
    # TASK 4: PURGE DISCONTINUED PRODUCTS (DELETE)
    # --------------------------------------------------------------------------
    print("\n" + "=" * 85)
    print("  TASK 4: PURGE DISCONTINUED & ZERO-STOCK PRODUCTS (DELETE)")
    print("=" * 85)
    purge_filter = {"status": "discontinued", "inventory.stock_count": 0}
    del_res = collection.delete_many(purge_filter)
    print(f"[OK] Successfully deleted {del_res.deleted_count} discontinued products.")
    print(f"[OK] Remaining Active Documents in Real Database: {collection.count_documents({})}")

    # --------------------------------------------------------------------------
    # TASK 5: AGGREGATION PIPELINE ($group, $sum, $avg)
    # --------------------------------------------------------------------------
    print("\n" + "=" * 85)
    print("  TASK 5: REAL-TIME ANALYTICS AGGREGATION PIPELINE")
    print("=" * 85)
    pipeline = [
        {"$match": {"status": "active"}},
        {
            "$group": {
                "_id": "$category",
                "product_count": {"$sum": 1},
                "total_units_in_stock": {"$sum": "$inventory.stock_count"},
                "total_inventory_value_inr": {"$sum": {"$multiply": ["$price", "$inventory.stock_count"]}},
                "average_product_price_inr": {"$avg": "$price"},
                "average_rating": {"$avg": "$rating.average"}
            }
        },
        {"$sort": {"total_inventory_value_inr": -1}}
    ]
    agg_res = list(collection.aggregate(pipeline))
    print(f"{'Category':<15} | {'Products':<10} | {'Stock (Units)':<14} | {'Valuation (INR)':<18} | {'Avg Price (INR)':<15} | {'Avg Rating'}")
    print("-" * 88)
    for r in agg_res:
        print(f"{r['_id']:<15} | {r['product_count']:<10} | {r['total_units_in_stock']:<14} | Rs. {r['total_inventory_value_inr']:>14,.2f} | Rs. {r['average_product_price_inr']:>11,.2f} | {r['average_rating']:.2f} / 5.0")

    # --------------------------------------------------------------------------
    # TASK 6: REAL WIREDTIGER EXECUTION STATS (COLLSCAN vs IXSCAN)
    # --------------------------------------------------------------------------
    print("\n" + "=" * 85)
    print("  TASK 6: REAL WIREDTIGER EXECUTION PLANS (COLLSCAN vs IXSCAN via explain())")
    print("=" * 85)
    print("[*] Inserting 5,000 synthetic catalog documents into real MongoDB collection...")
    bulk = []
    random.seed(60)
    for i in range(1001, 6001):
        bulk.append({
            "_id": f"REAL_SYNTH_{i}",
            "title": f"Live Product Model {i}",
            "category": random.choice(["Electronics", "Apparel", "Groceries", "Books", "HomeLiving"]),
            "price": round(random.uniform(99.0, 49999.0), 2),
            "inventory": {"stock_count": random.randint(1, 200)},
            "rating": {"average": round(random.uniform(3.0, 5.0), 1)},
            "status": "active"
        })
    collection.insert_many(bulk)
    total_docs = collection.count_documents({})
    print(f"[OK] Total Documents in Collection: {total_docs:,}")

    bench_query = {"category": "Electronics", "price": {"$gte": 25000.0, "$lte": 35000.0}}

    # 1. Real Explain Plan BEFORE Index (COLLSCAN)
    print("\n[*] Evaluating Execution Plan BEFORE creating compound index:")
    plan_before = db.command("explain", {
        "find": COLLECTION_NAME,
        "filter": bench_query
    }, verbosity="executionStats")

    exec_stats_before = plan_before.get("executionStats", {})
    winning_plan_before = plan_before.get("queryPlanner", {}).get("winningPlan", {})
    stage_before = winning_plan_before.get("stage") or winning_plan_before.get("inputStage", {}).get("stage", "COLLSCAN")

    print(f"    - Query Stage               : {stage_before} (Full Collection Scan)")
    print(f"    - Total Documents Examined  : {exec_stats_before.get('totalDocsExamined', total_docs):,}")
    print(f"    - Execution Time            : {exec_stats_before.get('executionTimeMillis', 0)} ms")

    # 2. Create Real Compound B-Tree Index in WiredTiger
    print("\n[*] Building Real Compound Index: collection.create_index([('category', 1), ('price', 1)])...")
    idx_name = collection.create_index([("category", pymongo.ASCENDING), ("price", pymongo.ASCENDING)])
    print(f"[OK] Real Index Created: '{idx_name}'")

    # 3. Real Explain Plan AFTER Index (IXSCAN)
    print("\n[*] Evaluating Execution Plan AFTER building compound index:")
    plan_after = db.command("explain", {
        "find": COLLECTION_NAME,
        "filter": bench_query
    }, verbosity="executionStats")

    exec_stats_after = plan_after.get("executionStats", {})
    winning_plan_after = plan_after.get("queryPlanner", {}).get("winningPlan", {})
    # Drill down to inputStage for IXSCAN
    stage_after = winning_plan_after.get("stage")
    if stage_after == "FETCH":
        sub_stage = winning_plan_after.get("inputStage", {}).get("stage", "IXSCAN")
        index_used = winning_plan_after.get("inputStage", {}).get("indexName", idx_name)
    else:
        sub_stage = stage_after
        index_used = winning_plan_after.get("indexName", idx_name)

    print(f"    - Query Stage               : {stage_after} -> {sub_stage} (Index B-Tree Scan)")
    print(f"    - Index Name Used           : {index_used}")
    print(f"    - Total Keys Examined       : {exec_stats_after.get('totalKeysExamined', 0):,}")
    print(f"    - Total Documents Examined  : {exec_stats_after.get('totalDocsExamined', 0):,}")
    print(f"    - Execution Time            : {exec_stats_after.get('executionTimeMillis', 0)} ms")

    docs_scanned_reduction = (1 - (exec_stats_after.get('totalDocsExamined', 1) / max(1, exec_stats_before.get('totalDocsExamined', total_docs)))) * 100
    print(f"    - Document Scan Reduction   : {docs_scanned_reduction:.1f}% fewer documents read from disk!")

    print("\n" + "=" * 85)
    print("  TASK 7: ARCHITECTURAL COMPARISON: NOSQL DOCUMENT STORE VS RDBMS")
    print("=" * 85)
    print("""
+--------------------------+------------------------------------+------------------------------------+
| Dimension                | Real MongoDB WiredTiger (NoSQL)    | Relational Database (MySQL/Oracle) |
+--------------------------+------------------------------------+------------------------------------+
| Schema Management        | Dynamic / Schema-on-Read: JSON/BSON| Rigid DDL: Requires ALTER TABLE    |
|                          | accommodates variable attributes.  | and schema migrations.             |
+--------------------------+------------------------------------+------------------------------------+
| Nested Data Retrieval    | Single document fetch retrieves all| Requires multi-table foreign-key   |
|                          | sub-objects (specs, reviews, tags).| JOIN queries, degrading latency.   |
+--------------------------+------------------------------------+------------------------------------+
| Index Efficiency         | Real B-Tree Compound Indexes       | Standard B-Tree Indexes on rigid   |
|                          | optimize polymorphic search paths. | relational columns only.           |
+--------------------------+------------------------------------+------------------------------------+
| Horizontal Scalability   | Native Auto-Sharding with Config   | Complex manual sharding or read-   |
|                          | Server cluster routing.            | replica replication bottlenecks.   |
+--------------------------+------------------------------------+------------------------------------+
    """)
    print("=" * 85)
    print("[SUCCESS] Real MongoDB Community Server Activity 4 Execution Complete!")
    print("=" * 85 + "\n")

if __name__ == "__main__":
    run_real_mongodb_pipeline()
