from typing import List
 
from pydantic import BaseModel, Field
 

from fastapi import APIRouter, status
from description.order_description import CreationDescription
from models.order import OrderGeneral
from service.order_rules import cart_checkout
 

order_route = APIRouter(prefix="/api/order",tags=["order"],) 
 
@order_route.post("/", summary="Criação de novo Carrinho de compras",description=CreationDescription.ORDER_CREATION_DESCRIPTION, status_code=status.HTTP_201_CREATED)
async def checkout(order: OrderGeneral):
    new_order = await cart_checkout(order)
    return new_order
 
