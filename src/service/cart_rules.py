 
from uuid import uuid4
from models.user import UserForAddress
 
import server.cart_server as cart_server
from models.cart import CartGeneral, CartUpdate, OrderItem
from models.cart import Cart
from service.user_rules import search_if_user_exists
 
from service.rules_exception import ExceptionNotFound
 
CAMPO_CODE = cart_server.CartField.CODE 
 
async def add_to_cart(user: UserForAddress,  order_item: OrderItem):
 
    await search_if_user_exists(user.user_code)
 
    order_item = await update_order_item_Price(order_item)  
   
    existingCart = await get_cart_by_user(user.user_code)
    
    if existingCart :
        existintProduct= await check_if_product_in_cart(order_item.product,existingCart)
        if existintProduct:
            return await change_cart_item(order_item, existingCart, existintProduct)            
        else:
            return await insert_into_cart(user,order_item,existingCart)              
    return await create_new_cart(user,order_item)  
 
 
 
 
async def create_new_cart(user: UserForAddress,  order_item: OrderItem) -> CartGeneral:      
    new_cart = dict(user = user.dict(),orderItem = [order_item.dict()],total_value = order_item.price, total_itens = order_item.quantity)
    new_cart[cart_server.CartField.CODE] = str(uuid4())
    await cart_server.create_new_cart(new_cart)  
    return {'sku' : order_item.product.sku}

 
async def update_order_item_Price(order_item: OrderItem):
   order_item.price = order_item.product.price * order_item.quantity
   return order_item

 
async def insert_into_cart(user: UserForAddress,  order_item: OrderItem, existingCart: Cart):
    await cart_server.insert_into_cart(order_item,existingCart)    
    return {'code' : order_item.product.sku }

 
async def change_cart_item(order_item: OrderItem, existintCart: Cart, existintProduct):
       
    sku = order_item.product.sku
    new_price = existintProduct['quantity'] * order_item.product.price
    filter =  {'code': existintCart['code'], 'orderItem.product.sku': str(sku) }
  
    update= {'$inc':  { 'total_value': new_price,
                        'total_itens': existintProduct['quantity'],
                        'orderItem.'+str(existintProduct['position'])+'.quantity': existintProduct['quantity'],
                        'orderItem.'+str(existintProduct['position'])+'.price': new_price}}

    return await cart_server.update_quantity(filter,update)
  
async def check_if_product_in_cart(sku: str, existingCart: Cart):
    print("Checkar se produto existe")
    for i,item in enumerate(existingCart['orderItem']):
        if item['product']['sku'] == sku:
            return {'position': i, 'quantity' : item['quantity'], 'price': item['price'], 'unit_price': item['product']['price']}
    return None
   
 
async def update_quantity(cartUpdate: CartUpdate):
    
    existingCart = await get_cart_by_user(cartUpdate.user.user_code)
    existintProduct= await check_if_product_in_cart(cartUpdate.product_sku,existingCart)
    old_price = existintProduct['price']
    old_quantity = existintProduct['quantity']
    price = cartUpdate.quantity * existintProduct['unit_price']
    filter =  {'code': existingCart['code'], 'orderItem.product.sku': cartUpdate.product_sku}
    update= {'$inc':  { 'total_value': price - old_price,
                        'total_itens':cartUpdate.quantity-old_quantity,
                        'orderItem.'+str(existintProduct['position'])+'.quantity': cartUpdate.quantity-old_quantity,
                        'orderItem.'+str(existintProduct['position'])+'.price': price - old_price}}

    return await cart_server.update_quantity(filter,update)
 
 
 
async def get_cart_by_user(code: str):
    #TODO pesquisar se o carrinho existe pelo id do usuario
    cart = await cart_server.get_cart_by_user_id(code)    
    return cart
 
async def remove_cart(code : str): 
    ##TODO E um cart ou um produto??? Implementar
    remove = await cart_server.delete_cart_by_code(code) 
    if not remove:
        raise ExceptionNotFound("O Carrinho ja foi removido")

# async def remove_from_cart(cartProduct : CartProduct): 
#     ##TODO E um cart ou um produto??? Implementar
#     filter = {"code": cartProduct.code, "orderItem.product.sku": cartProduct.product_sku}
#     remove = await cart_server.remove_from_cart(filter) 
#     if not remove:
#         raise ExceptionNotFound("O Carrinho ja foi removido")
 
 
 # async def update_by_code(code: str, cart: CartUpdate):
   
#     await search_by_code(code, True)
 
#     data = dict(cart)
#     data = {k: v for k, v in data.items() if v is not None}
 
#     await cart_server.update_cart_by_code(
#         code, data
#     )
 
 
 
