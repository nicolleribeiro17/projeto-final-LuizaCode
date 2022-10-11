from typing import List
 
from pydantic import BaseModel, Field
from models.user import UserForAddress
from fastapi import APIRouter, status
from models.cart import Cart, OrderItem
import service.cart_rules as cart_rules
 
# Minha rota API de Usuários
cart_route = APIRouter(prefix="/api/cart",tags=["Carts"],)
 
CART_CREATION_DESCRIPTION = """
Criação de um novo usuário. Para registrar um novo usuário:
 
Se o usuário for criado corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`codigo`, que é o código do novo usuário em nosso sistema.
"""
 
# Colocamos este modelo aqui, SOMENTE para ficar perto da documentação.
# Seria apropriado criar um 'modelo' para cada erro??
 
 
@cart_route.post("/", summary="Adicionar item ao carrinho",description=CART_CREATION_DESCRIPTION, status_code=status.HTTP_201_CREATED)
async def add_to_cart(user: UserForAddress,  order_item: OrderItem):
    new_cart = await cart_rules.add_to_cart(user,order_item)
    return new_cart
 
@cart_route.put("/update/{code}",status_code=status.HTTP_202_ACCEPTED,
    summary="Atualizar quantidade do produto",
    description="Atualiza um usuário pelo código",
)
async def update_quantity(cart : OrderItem, quantity: int):
    await cart_rules.update_quantity(cart,quantity)
 
 
@cart_route.delete("/{code}", status_code=status.HTTP_202_ACCEPTED, summary="Remoção do usuário",
    description="Remove o produto do carrinho")
async def remove_from_cart(cart : OrderItem):
    await cart_rules.remove_from_cart(cart)
 
 
 
 



 
 