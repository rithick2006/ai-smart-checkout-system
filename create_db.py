import sqlite3
import json

DB = "products.db"

def create_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    # Drop old table if exists
    c.execute("DROP TABLE IF EXISTS Products")

    c.execute("""CREATE TABLE Products (
                    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Price REAL,
                    Stock INTEGER,
                    ClassID INTEGER
                )""")

    # Load class names
    with open("class_names.json", "r") as f:
        class_names = json.load(f)

    # Example Indian prices
    sample_prices = [12, 40, 20]  # Maggi, Coca Cola, Lays
    sample_stock = [200, 150, 180]

    for idx, name in enumerate(class_names):
        price = sample_prices[idx] if idx < len(sample_prices) else 50
        stock = sample_stock[idx] if idx < len(sample_stock) else 100
        c.execute("INSERT INTO Products (Name, Price, Stock, ClassID) VALUES (?, ?, ?, ?)",
                  (name, price, stock, idx))

    conn.commit()
    conn.close()
    print("✅ Database created as products.db")

if __name__ == "__main__":
    create_db()
