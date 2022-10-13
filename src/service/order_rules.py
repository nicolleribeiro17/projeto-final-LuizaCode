from uuid import uuid4
from models.cart import Cart
from models.order import OrderGeneral 

from server import order_server
from service.address_rules import get_user_address_order
from service.cart_rules import get_cart_by_user_order
from service.user_rules import search_if_user_exists


 
CAMPO_CODE = order_server.OrderField.CODE


#Fecha o pedido e deleta o carrinho
async def cart_checkout(order: OrderGeneral):
    
    await search_if_user_exists(order.user.code) 
    address = await get_user_address_order(order)  
    cart = await get_cart_by_user_order(order.user.code)
    return await create_new_order(order,address,cart)

# cria o pedido no banco
async def create_new_order(order: OrderGeneral, address: dict, cart: Cart):
    final_order = await close_order(order,address,cart)
    await order_server.create_new_order(final_order) 
    #await remove_cart(cart.code)  ## Apos encerrar o pedido deletar o carrinho
    return final_order['code']

#Processa os dados do pedido
async def close_order(order: OrderGeneral,address,cart: Cart):
    cart_value = cart['total_value']
    final_value = cart_value - order.order.discount
    order= order.dict()
    order["code"] = str(uuid4())
    order["order"]["totalPrice"] = final_value
    order["order"]["numberItens"] = cart['total_itens']
    order["address"] = address.dict()
    order["cart"] = cart['orderItem']
    return order