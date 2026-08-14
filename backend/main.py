import sqlite3
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import OrderStatus

app = FastAPI(title="Northstar Support API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "northstar.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/api/orders/{order_id}", response_model=OrderStatus)
def get_order(order_id: str):
    conn = get_db_connection()
    order = conn.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,)).fetchone()
    conn.close()
    
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return dict(order)

# TODO: ahmedabdy590-spec (Ahmed) - Build the logic for this endpoint to query the database.
@app.get("/api/returns/{order_id}")
def get_return(order_id: str):
    return {"message": "Endpoint not implemented yet"}

# TODO: ahmedabdy590-spec (Ahmed) - Build the logic for this endpoint to query the database.
@app.get("/api/stock/{sku}")
def get_stock(sku: str):
    return {"message": "Endpoint not implemented yet"}
