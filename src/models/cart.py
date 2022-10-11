from typing import Optional, List
from pydantic import BaseModel,Field
from models.order_item import  OrderItem
from models.user import UserForAddress


class Cart(BaseModel):
    #Esse codigo e a interface do carrinho de mercado. Ele recebe os produtos ja agrupados com sua quantidade e preco
    #Ele e conjunto de order items-
    user: UserForAddress
    orderItem: List[OrderItem] = []
    total_value: float
    total_itens: int

class CartCode(BaseModel):
    code: str = Field(..., description="Código do usuário, no formato uuid v4")
   
class CartGeneral(CartCode, Cart):
    ...
  
  

    
    
