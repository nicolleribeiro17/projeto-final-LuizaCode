
from turtle import update
from typing import List, Optional
from uuid import uuid4
from models import order_item
from models.user import UserForAddress
from server import order_item_server
 
import server.cart_server as cart_server
from models.cart import CartGeneral, OrderItem
from models.cart import Cart
from service.user_rules import search_if_user_exists
 
from service.rules_exception import ExceptionNotFound
 
CAMPO_CODE = cart_server.CartField.CODE
 
 
async def add_to_cart(user: UserForAddress,  order_item: OrderItem):
    #TODO checar se existe um carrinho para aquele usuario (criar funcao get_cart_by_user)
    #Se existir-continuar , se nao existir- criar carrinho ( criar NO CART create_new_cart) 
    await search_if_user_exists(user.user_code) 

    order_item = await update_order_item_Price(order_item)  
   
    existingCart = await get_cart_by_user(user.user_code)
    
    if existingCart is not None:
        existintProduct= await check_if_product_in_cart(order_item,existingCart)
        if existintProduct is None:
            return await insert_into_cart(user,order_item,existingCart)              
        else:
            new_quantity = existintProduct['quantity'] + order_item.quantity
            return await update_quantity(order_item, existingCart, new_quantity)  
    return await create_new_cart(user,order_item)  
 


 
async def create_new_cart(user: UserForAddress,  order_item: OrderItem) -> CartGeneral:      
    new_cart = dict(user = user.dict(),orderItem = [{order_item.product.sku: order_item.dict()}],total_value = order_item.price, total_itens = order_item.quantity)
    new_cart[cart_server.CartField.CODE] = str(uuid4())
    await cart_server.create_new_cart(new_cart)  
    return {'sku' : order_item.product.sku}
 
async def update_order_item_Price(order_item: OrderItem):
   order_item.price = order_item.product.price * order_item.quantity
   return order_item

async def insert_into_cart(user: UserForAddress,  order_item: OrderItem, existingCart: Cart):
    await cart_server.insert_into_cart(order_item,existingCart)    
    return {'code' : order_item.product.sku } 
   
 
async def update_quantity(order_item: OrderItem, existintCart: Cart, quantity):
    #TODO Metodo para alterar a quantidade de um determinado produto
    sku = order_item.product.sku
    new_price = quantity * order_item.product.price
    filter= "orderItem.2.price : "+ str(new_price) + " , orderItem.2.quantity : "+ str(quantity)
    return await cart_server.update_quantity(existintCart['code'], filter)
  
 
async def check_if_product_in_cart(order_item: OrderItem, existingCart: Cart):
    return dict((key,d[key]) for d in existingCart['orderItem'] for key in d).get(order_item.product.sku)
    


 
 
 
async def get_cart_by_user(code: str):
    #TODO pesquisar se o carrinho existe pelo id do usuario
    cart = await cart_server.get_cart_by_user_id(code)    
    return cart
 
async def remove_from_cart(cart : OrderItem):
 
    ##TODO E um cart ou um produto??? Implementar
    remove = await cart_server.delete_by_code(cart)
 
    if not remove:
        raise ExceptionNotFound("Usuário não encontrada") 
 
 
 # async def update_by_code(code: str, cart: CartUpdate):
   
#     await search_by_code(code, True)
 
#     data = dict(cart)
#     data = {k: v for k, v in data.items() if v is not None}
 
#     await cart_server.update_cart_by_code(
#         code, data
#     )
 

