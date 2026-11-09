// ==============================================================================
//  ACTIVITY 4: REAL MONGODB CLI QUERIES - USN: 1MS24CI060
//  Execute via: mongosh real_store_1MS24CI060 queries.js
// ==============================================================================

print("\n--- 1. TOTAL DOCUMENTS IN WIREDTIGER COLLECTION ---");
print("Document Count:", db.products_catalog_060.countDocuments());

print("\n--- 2. ACTIVE B-TREE INDEXES ---");
printjson(db.products_catalog_060.getIndexes());

print("\n--- 3. SAMPLE ELECTRONICS DOCUMENT (Polymorphic Specs) ---");
printjson(db.products_catalog_060.findOne({_id: "PROD_1MS24CI060_001"}));

print("\n--- 4. SAMPLE GROCERY DOCUMENT (Food Attributes) ---");
printjson(db.products_catalog_060.findOne({_id: "PROD_1MS24CI060_006"}));

print("\n--- 5. CATEGORY AGGREGATION PIPELINE (Stock & Valuation) ---");
printjson(db.products_catalog_060.aggregate([
  {
    $group: {
      _id: "$category",
      totalProducts: { $sum: 1 },
      avgPrice: { $avg: "$price" },
      totalStock: { $sum: "$inventory.stock_count" },
      totalValuation: { $sum: { $multiply: ["$price", "$inventory.stock_count"] } }
    }
  },
  { $sort: { totalValuation: -1 } }
]).toArray());
