from app.db import init_db, add_product

# Step 1: Create table
init_db()

# Step 2: Add products (match class_names.json order!)
add_product(0, "coca_cola", 40.0)   # class 0 = coca_cola
add_product(1, "lays", 20.0)  # class 1 = lays
add_product(2, "maggi", 15.0)  # class 2 = maggi

print("✅ Database initialized with correct mapping")
