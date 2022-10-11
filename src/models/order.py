from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from models.cart import  Cart
from models.address import  Address
from models.user import UserForAddress

class Order(BaseModel):
    #E o pedido final que ja nao vai mais ser modificado. Ele contem um cart contem 
    # os produtos ja agrupados com sua quantidade e preco   
    createdAt: datetime = Field(default= datetime.now())
    discount: float = Field(...,ge=0.01)
    totalPrice: float = Field(...,ge=0.01) ## cart.price - discount    
    paymentId: str = Field(None,min_lenght = 24, max_lenght = 24)    
    status: int = Field(...,ge=1)  ## 1- pago, 2- Aguardando pagamento..
      
class OrderGeneral(UserForAddress,Cart,Address,Order):
    ...
