# Built by Jesse Vincent (jdilemmax) - Order Status API
# Built by Ahmed Abdi Ibrahim (ahmedabdy590-spec) - Returns & Stock APIs
from pydantic import BaseModel
from typing import Optional

class OrderStatus(BaseModel):
    order_id: str
    customer_name: str
    status: str
    shipping_date: Optional[str] = None
    tracking_number: Optional[str] = None

class ReturnRequest(BaseModel):
    return_id: str
    order_id: str
    reason: str
    status: str
    return_date: Optional[str] = None

class StockItem(BaseModel):
    product_id: str
    product_name: str
    quantity: int
    price: float
    in_stock: bool
