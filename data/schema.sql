CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    status TEXT NOT NULL,
    shipping_date TEXT,
    tracking_number TEXT
);

-- TODO: ginahAphane (Ginah) - Create the 'returns' and 'products' tables and seed 15+ records.
CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS returns (
    return_id TEXT PRIMARY KEY,
    order_id TEXT NOT NULL,
    return_date TEXT NOT NULL,
    reason TEXT  NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
