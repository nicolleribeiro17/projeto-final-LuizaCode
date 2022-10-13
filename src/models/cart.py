from typing import Optional, List
from pydantic import BaseModel,Field
from models.order_item import  OrderItem
from models.user import UserForAddress


class Cart(BaseModel):
    user: UserForAddress
    orderItem: List[OrderItem] = []
    total_value: float
    total_itens: int

class CartCode(BaseModel):
    code: str = Field(..., description="Código do carrinho, no formato uuid v4")
   
class CartGeneral(BaseModel):
    cart_code:CartCode
    cart:Cart
  
class CartUpdate(BaseModel):
    user: UserForAddress
    product_sku: str
    quantity : int

    
    
