CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    status TEXT NOT NULL,
    shipping_date TEXT,
    tracking_number TEXT
);

-- TODO: ginahAphane (Ginah) - Create the 'returns' and 'products' tables here
