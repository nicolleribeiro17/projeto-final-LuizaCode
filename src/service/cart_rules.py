 
from uuid import uuid4
from models.user import UserForAddress
 
import server.cart_server as cart_server
from models.cart import CartGeneral, CartUpdate, OrderItem
from models.cart import Cart
from service.user_rules import search_if_user_exists
 
from service.rules_exception import ExceptionNotFound
 
CAMPO_CODE = cart_server.CartField.CODE 
 
# Cria cart
async def add_to_cart(user: UserForAddress,  order_item: OrderItem):
 
    await search_if_user_exists(user.user_code)
 
    order_item = await update_order_item_Price(order_item)  
   
    existingCart = await get_cart_by_user(user.user_code)
    
    if existingCart :
        existintProduct= await check_if_product_in_cart(order_item.product.sku,existingCart)
        if existintProduct:
            return await change_cart_item(order_item, existingCart, existintProduct)            
        else:
            return await insert_into_cart(user,order_item,existingCart)              
    return await create_new_cart(user,order_item)  
  
#Cria um carrinho quando nao existe nenhum
async def create_new_cart(user: UserForAddress,  order_item: OrderItem) -> CartGeneral:      
    new_cart = dict(user = user.dict(),orderItem = [order_item.dict()],total_value = order_item.price, total_itens = order_item.quantity)
    new_cart[cart_server.CartField.CODE] = str(uuid4())
    await cart_server.create_new_cart(new_cart)  
    return {'sku' : order_item.product.sku}

#Insere produto no carrinho
async def insert_into_cart(user: UserForAddress,  order_item: OrderItem, existingCart: Cart):
    await cart_server.insert_into_cart(order_item,existingCart)    
    return {'code' : order_item.product.sku }

#Atualiza o valordo carrinho
async def update_order_item_Price(order_item: OrderItem):
   order_item.price = order_item.product.price * order_item.quantity
   return order_item

#Atualiza a quantidade de um produto no carrinho 
async def change_cart_item(order_item: OrderItem, existintCart: Cart, existintProduct):
    
    sku = order_item.product.sku
    new_price = order_item.quantity * order_item.product.price
    filter =  {'code': existintCart['code'], 'orderItem.product.sku': str(sku) }
  
    update= {'$inc':  { 'total_value': new_price,
                        'total_itens': order_item.quantity,
                        'orderItem.'+str(existintProduct['position'])+'.quantity': order_item.quantity,
                        'orderItem.'+str(existintProduct['position'])+'.price': new_price}}

    return await cart_server.update_quantity(filter,update)

#Checa se ja existe o produto no carrinho 
async def check_if_product_in_cart(sku: str, existingCart: Cart):
    for i,item in enumerate(existingCart['orderItem']):
        if item['product']['sku'] == sku:
            return {'position': i, 'quantity' : item['quantity'], 'price': item['price'], 'unit_price': item['product']['price']}
    return None
   
#Quando ja houver o produto no carrinho, ele altera a quantidade
async def update_quantity(cartUpdate: CartUpdate):    
    existingCart = await get_cart_by_user(cartUpdate.user.user_code)
    existintProduct= await check_if_product_in_cart(cartUpdate.product_sku,existingCart)
    old_price = existintProduct['price']
    old_quantity = existintProduct['quantity']
    price = cartUpdate.quantity * existintProduct['unit_price']

    empty_cart = await check_empty_cart(cartUpdate,existingCart)

    if empty_cart:
        await remove_cart(existingCart['code'])    

    filter =  {'code': existingCart['code'], 'orderItem.product.sku': cartUpdate.product_sku}
    update= {'$inc':  { 'total_value': price - old_price,
                        'total_itens':cartUpdate.quantity-old_quantity,
                        'orderItem.'+str(existintProduct['position'])+'.quantity': cartUpdate.quantity-old_quantity,
                        'orderItem.'+str(existintProduct['position'])+'.price': price - old_price}}

    return await cart_server.update_quantity(filter,update)
 
 
 #Retorna um carrinho pelo codigo do usuario
async def get_cart_by_user(code: str):
    cart = await cart_server.get_cart_by_user_id(code)    
    return cart

async def check_empty_cart(cartUpdate: CartUpdate, existingCart: Cart):
    if (cartUpdate.quantity == 0 and len(existingCart['orderItem']) == 1):
        return True
    return False

#Retorna um carrinho pelo codigo do usuario para fechar o pedido
async def  get_cart_by_user_order(code: str):
    cart = await cart_server.get_cart_by_user_id(code)    
    if not cart:
        raise ExceptionNotFound("O carrinho esta vazio")
    return cart

#Deleta o carrinho
async def remove_cart(code : str): 
    remove = await cart_server.delete_cart_by_code(code) 
    if not remove:
        raise ExceptionNotFound("O Carrinho ja foi removido")
