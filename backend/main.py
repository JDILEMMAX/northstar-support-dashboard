# Built by Jesse Vincent (jdilemmax) - Order Status API
# Built by Ahmed Abdi Ibrahim (ahmedabdy590-spec) - Returns & Stock APIs
import sqlite3
import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import OrderStatus, ReturnRequest, StockItem

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

@app.get("/api/returns/{order_id}", response_model=ReturnRequest)
def get_return(order_id: str):
    conn = get_db_connection()
    return_req = conn.execute("SELECT * FROM returns WHERE order_id = ?", (order_id,)).fetchone()
    conn.close()
    
    if return_req is None:
        raise HTTPException(status_code=404, detail="Return request not found")
    
    # Map status if it doesn't exist in DB
    result = dict(return_req)
    if 'status' not in result:
        result['status'] = "Processing"
    return result

@app.get("/api/stock/{sku}", response_model=StockItem)
def get_stock(sku: str):
    conn = get_db_connection()
    stock = conn.execute("SELECT * FROM products WHERE product_id = ?", (sku,)).fetchone()
    conn.close()
    
    if stock is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    result = dict(stock)
    if 'in_stock' not in result:
        result['in_stock'] = result['quantity'] > 0
    return result