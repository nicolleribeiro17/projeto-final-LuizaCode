from typing import List
 
from pydantic import BaseModel, Field
 
#import service.order_rules as order_rules
from fastapi import APIRouter, status
from models.order import Order
from models.address import Address
from server.order_server import create_order_user, get_order_by_user_email
 
# Minha rota API de Carrinho de comprass
order_route = APIRouter(prefix="/api/order",tags=["order"],)
 
ORDER_CREATION_DESCRIPTION = """
Criação de um novo Carrinho de compras para o usuario:
 
Se o Carrinho de compras for criado corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`codigo`, que é o código do novo Carrinho de compras em nosso sistema.
"""
 
@order_route.post("/", summary="Criação de novo Carrinho de compras",description=ORDER_CREATION_DESCRIPTION, status_code=status.HTTP_201_CREATED)
async def checkout(order: Order,address: Address):
    new_order = await create_order_user(order)
    return new_order
 
