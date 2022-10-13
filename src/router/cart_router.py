from models.user import UserForAddress
from fastapi import APIRouter, status
 
from models.cart import CartUpdate, OrderItem
import service.cart_rules as cart_rules
from description.cart_description import CreationDescription, UpdateDescription, DeleteDescription
 
cart_route = APIRouter(prefix="/api/cart",tags=["Carts"],)
 
@cart_route.post("/", summary="Adicionar item ao carrinho",description=CreationDescription.CART_CREATION_DESCRIPTION,
status_code=status.HTTP_201_CREATED)
async def add_to_cart(user: UserForAddress,  order_item: OrderItem):
    new_cart = await cart_rules.add_to_cart(user,order_item)
    return new_cart
 
@cart_route.put("/update",status_code=status.HTTP_200_OK,
summary="Atualizar quantidade do produto", description=UpdateDescription.CART_UPDATE_DESCRIPTION,)
async def update_quantity(cartUpdate : CartUpdate):
    await cart_rules.update_quantity(cartUpdate)
 
 
@cart_route.delete("/{code}", status_code=status.HTTP_200_OK, summary="Remoção do usuário",
    description=DeleteDescription.CART_DELETE_DESCRIPTION)
async def remove_cart(code : str):
    await cart_rules.remove_cart(code)
 

   
 
 
 
 
 
 
 
 
 
