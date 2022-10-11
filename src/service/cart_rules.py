
from typing import List, Optional
from uuid import uuid4
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
    existinguser = await search_if_user_exists(user.user_code)
    if not existinguser:
        raise ExceptionNotFound("Usuário não encontrado")
    existingCart = await get_cart_by_user(user.user_code)
    if existingCart is None:
        return await create_new_cart(user,order_item)        
    return await insert_into_cart(user,order_item,existingCart)    
 
 

 
async def create_new_cart(user: UserForAddress,  order_item: OrderItem) -> CartGeneral:  
    
    order_item = order_item.dict()  
    value = order_item['product']['price'] * order_item['quantity']   
    order_item[order_item_server.OrderItemField.PRICE] = value
    new_cart = dict(user = user.dict(),orderItem = [{order_item['product']['sku']: order_item}],total_value = value, total_itens = order_item['quantity'])
    new_cart[cart_server.CartField.CODE] = str(uuid4())
    await cart_server.create_new_cart(new_cart)  
    # cart_geral = CartGeneral(**new_cart)
    return {'code' : new_cart['code']}
 
async def calculate_cart_value(order_item: OrderItem) -> float:
    total = 0
    for item in order_item:
        print(order_item.name)


async def insert_into_cart(user: UserForAddress,  order_item: OrderItem, existingCart: Cart):
    #TODO inserir o produt no carrinho -- Antes e preciso validar se o produto ja existe no carrinho,
    #  e caso ja exista fazer um update na quantidade de itens
    existintProduct= await check_if_product_in_cart(order_item,existingCart)
    if not existintProduct :
        order_item = order_item.dict()  
        value = order_item['product']['price'] * order_item['quantity']   
        order_item[order_item_server.OrderItemField.PRICE] = value
        await cart_server.insert_into_cart(order_item,existingCart)     
    # await update_quantity(user,order_item,existingCart)   
    # return
 
async def update_quantity(cart: OrderItem, quantity:int):
    #TODO Metodo para alterar a quantidade de um determinado produto
    return
   
 
async def check_if_product_in_cart(order_item: OrderItem, existingCart: Cart):

    #TODO melhorar esse if aninhado
    existintProduct = False
    for item in existingCart['orderItem']:
        for key in item:
            if(key == order_item.product.sku):
                existintProduct = True
    
    return existintProduct



 
 
 
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
 

