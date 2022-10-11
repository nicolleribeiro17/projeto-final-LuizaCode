from typing import List, Optional
from bson.json_util import dumps
import json
from models.cart import Cart

from models.order_item import OrderItem

 
from .database import get_collection
 
class CartField:
    CODE = "code"
   
 
cart_collection = get_collection("cart")
 
async def get_by_code(cart_code: str) -> Optional[dict]:
    filter = { CartField.CODE: cart_code }
    cart = await cart_collection.find_one(filter)
    return cart
 
async def get_all() -> List[dict]:
    filter = {}
    cursor_pesquisa = cart_collection.find(filter)
    list_all = [cart async for cart in cursor_pesquisa]
    return list_all
 
async def get_cart_by_user_id(code: str) -> Optional[dict]:
    cart = await cart_collection.find_one({"user.user_code" : code})
    if cart:
        return json.loads(dumps(cart))
 
async def create_new_cart(new_cart: dict) -> dict:
    await cart_collection.insert_one(new_cart)
    return new_cart
 
async def delete_by_code(cart_code: str) -> bool:
    filter = {CartField.CODE: cart_code}
    result = await cart_collection.delete_one(filter)
    removed = result.deleted_count > 0
    return removed
 
async def insert_into_cart(order_item: OrderItem, existingCart: Cart):
  
    value = existingCart['total_value'] + order_item['price']
    print(value)
    tot_item = existingCart['total_itens'] + order_item['quantity']
    print(tot_item)
    try:  
        cart = await cart_collection.update_one(
            {'code': existingCart['code']},
            {"$addToSet": {"orderItem":{order_item['product']['sku']: order_item}},
            "total_value": value,
            "total_itens": tot_item}       
            
        ) 
        if cart.modified_count:
            return cart.modified_count 
        return None
    except Exception as e:
        print(f'insert_into_cart.error: {e}')    
    
 
