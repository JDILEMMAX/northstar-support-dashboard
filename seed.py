import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "northstar.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

def seed_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Load schema
    with open(SCHEMA_PATH, "r") as f:
        cursor.executescript(f.read())

    # Clear old data
    cursor.execute("DELETE FROM returns")
    cursor.execute("DELETE FROM orders")
    cursor.execute("DELETE FROM products")

    # 15 products: id, name, quantity, price
    mock_products = [
        ("P001", "Laptop", 15, 15999.99), ("P002", "Mouse", 50, 299.00), ("P003", "Keyboard", 30, 499.99),
        ("P004", "Monitor", 20, 3499.00), ("P005", "Headphones", 40, 899.50), ("P006", "Webcam", 25, 650.00),
        ("P007", "USB Cable", 100, 49.99), ("P008", "Desk Chair", 10, 2200.00), ("P009", "Desk Lamp", 35, 350.00),
        ("P010", "Microphone", 18, 1200.00), ("P011", "Tablet", 12, 4999.99), ("P012", "Speaker", 22, 750.00),
        ("P013", "SSD 1TB", 45, 1299.00), ("P014", "RAM 16GB", 60, 850.00), ("P015", "Graphics Card", 8, 8999.00)
    ]
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", mock_products)

    # 15 orders: id, customer, status, date, tracking
    mock_orders = [
        ("ORD12345", "Jane Doe", "Delivered", "2026-08-10", "TRK001"),
        ("ORD12346", "John Smith", "Processing", None, None),
        ("ORD12347", "Alice Johnson", "Delivered", "2026-08-09", "TRK002"),
        ("ORD12348", "Bob Lee", "Shipped", "2026-08-12", "TRK003"),
        ("ORD12349", "Sara Kim", "Processing", None, None),
        ("ORD12350", "Mike Chen", "Delivered", "2026-08-05", "TRK004"),
        ("ORD12351", "Emma Davis", "Shipped", "2026-08-13", "TRK005"),
        ("ORD12352", "Liam Wilson", "Processing", None, None),
        ("ORD12353", "Olivia Brown", "Delivered", "2026-08-03", "TRK006"),
        ("ORD12354", "Noah Taylor", "Shipped", "2026-08-14", "TRK007"),
        ("ORD12355", "Ava Moore", "Processing", None, None),
        ("ORD12356", "Ethan Clark", "Delivered", "2026-08-11", "TRK008"),
        ("ORD12357", "Mia Lewis", "Shipped", "2026-08-15", "TRK009"),
        ("ORD12358", "James Hall", "Processing", None, None),
        ("ORD12359", "Sophia Allen", "Delivered", "2026-08-07", "TRK010")
    ]
    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", mock_orders)

    # 14 returns: id, order_id, date, reason
    mock_returns = [
        ("R001", "ORD12345", "2026-08-12", "Damaged on arrival"), ("R002", "ORD12347", "2026-08-11", "Wrong item sent"),
        ("R003", "ORD12350", "2026-08-08", "Customer changed mind"), ("R004", "ORD12353", "2026-08-06", "Defective product"),
        ("R005", "ORD12356", "2026-08-13", "Late delivery"), ("R006", "ORD12359", "2026-08-09", "Size issue"),
        ("R007", "ORD12345", "2026-08-14", "Missing parts"), ("R008", "ORD12347", "2026-08-15", "Not as described"),
        ("R009", "ORD12350", "2026-08-10", "Faulty battery"), ("R010", "ORD12353", "2026-08-07", "Screen cracked"),
        ("R011", "ORD12356", "2026-08-16", "Overheating"), ("R012", "ORD12359", "2026-08-11", "No power"),
        ("R013", "ORD12345", "2026-08-17", "Warranty claim"), ("R014", "ORD12347", "2026-08-18", "Software issue"),
        ("R015", "ORD12350", "2026-08-19", "Color mismatch")]
    cursor.executemany("INSERT INTO returns VALUES (?, ?, ?, ?)", mock_returns)

    # Display the number of records in each table
    cursor.execute("SELECT COUNT(*) FROM products")
    print(f"Number of products: {cursor.fetchone()[0]}")

    cursor.execute("SELECT COUNT(*) FROM orders")
    print(f"Number of orders: {cursor.fetchone()[0]}")

    cursor.execute("SELECT COUNT(*) FROM returns")
    print(f"Number of returns: {cursor.fetchone()[0]}")

    conn.commit()
    conn.close()
    print("Database seeded successfully with 15+ records in each table.")

seed_database()
ss