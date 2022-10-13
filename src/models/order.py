from datetime import datetime
from email.headerregistry import Address
from typing import Optional, List
from pydantic import BaseModel, Field
from models.address import orderAddress
from models.user import UserCode

class Order(BaseModel):
    createdAt: datetime = Field(default= datetime.now())
    discount: float = Field(default= 0.00,ge=0.00)
    totalPrice: Optional[float] ## O Valor e fechado no checkout
    numberItens:Optional[int]
    paymentId: Optional[str]   
    status: int = Field(default= 1,ge=1)  ## 1- Aguardando pagamento, 2- pago..
      
class OrderGeneral(BaseModel):
    user: UserCode
    address: Optional[orderAddress]
    order: Order
    