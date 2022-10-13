from ast import List
from uuid import uuid4
from bson import ObjectId
from bson.objectid import ObjectId
from models.user import UserForAddress
from models.order import Order
 
from .database import get_collection
 
 
order_collection = get_collection("order")
 
class OrderField:
    CODE = "code"
   

async def create_new_order(new_order: dict):  
    try:
        await order_collection.insert_one(new_order)
        return new_order  
    except Exception as e:
        print(f'create_new_order.error: {e}')    
 
 