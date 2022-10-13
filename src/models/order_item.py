from dataclasses import Field
from token import OP
from typing import Optional
from pydantic import BaseModel, Field
from models.product import  Product

class OrderItem(BaseModel):
    product: Product
    quantity: int 
    price:Optional[float]
    
   
class OrderItemUpdate(BaseModel):
    quantity: int 

