from typing import Dict, List, Optional
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
 
async def delete_cart_by_code(cart_code: str) -> bool:
    filter = {CartField.CODE: cart_code}
    result = await cart_collection.delete_one(filter)
    removed = result.deleted_count > 0
    return removed
 


async def insert_into_cart(order_item: OrderItem, existingCart: Cart):
  
    try:  
        cart = await cart_collection.update_one(
            {'code': existingCart['code']},
            {"$addToSet": {"orderItem": order_item.dict() }}
            
        ) 
        cart = await cart_collection.update_one(
            {'code': existingCart['code']},         
            {"$set": {"total_value":existingCart['total_value'] + order_item.price, 
                      "total_itens": existingCart['total_itens'] + order_item.quantity}})

        if cart.modified_count:
            return cart.modified_count 
        return None
    except Exception as e:
        print(f'insert_into_cart.error: {e}')    

async def update_quantity(filter: Dict, update: Dict):    
    try: 
        cart = await cart_collection.update_one(filter,update)      
    except Exception as e:
        print(f'update_quantity.error: {e}')    
 


# async def remove_from_cart(filter: dict) -> bool:
    
#     result = await cart_collection.update_one(filter,
#     { "$pull": {"orderItem.product.$.sku": '13555'}})
#     removed = result.deleted_count > 0
#     return removed


# def update_item(self, product, quantity, option_values=[]):
#         """
#         To update :class:`CartItem` object quantity.
        
#         :param product: Unique id or name of :class:`Product` object or instance of :class:`Product`.
#         :param quantity: Updated quantity.
#         :param option_values: Option values of the product(default []).
#         """
#         if not isinstance(quantity, (int, float)):
#             raise TypeError('quantity field value must be integer or float type', 'price')
#         elif not (quantity or quantity >= 1):
#             raise ValueError('quantity field value must be greater then 1')
            
#         cart_item = self.find_item(product, option_values)
        
#         if cart_item:
#             cart_item.update_quantity(quantity)

# def update_quantity(self, quantity):
#     """
#     To update existing quantity related to :class:`Product` object.
#     :param quantity: Product quantity.
#     """
#     self.quantity = quantity