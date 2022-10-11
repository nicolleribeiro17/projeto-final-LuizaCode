from dataclasses import Field
from token import OP
from typing import Optional
from pydantic import BaseModel, Field
from models.product import  Product

class OrderItem(BaseModel):
    #Esse codigo e a interface que mostra um item dentro do carrinho - ex: Hamburguer , 2 unidades , valor = 30
    product: Product
    quantity: int 
    price:Optional[float]
    
   
class OrderItemUpdate(BaseModel):
    quantity: int 

