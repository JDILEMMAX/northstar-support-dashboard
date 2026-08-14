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

    # Seed mock records
    cursor.execute("DELETE FROM orders")
    mock_orders = [
        ("ORD12345", "Jane Doe", "Shipped", "2026-08-10", "TRK987654321"),
        ("ORD12346", "John Smith", "Processing", None, None),
        ("ORD12347", "Alice Johnson", "Delivered", "2026-08-01", "TRK123456789")
    ]
    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", mock_orders)

    conn.commit()
    conn.close()
    print("Database seeded successfully.")

# TODO: ginahAphane (Ginah) - Expand the seed script to 15+ mock records for all tables.

if __name__ == "__main__":
    seed_database()
