from pydantic import BaseModel
from typing import Optional

class OrderStatus(BaseModel):
    order_id: str
    customer_name: str
    status: str
    shipping_date: Optional[str] = None
    tracking_number: Optional[str] = None

# TODO: ahmedabdy590-spec (Ahmed) - Create the Returns and Stock models here.
