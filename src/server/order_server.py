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
   
 
# Cria carrinho associado ao usuario
async def create_order_user(user: UserForAddress, order: Order):  
    existingOrder = await get_order_user_code(user.user_code)
    if existingOrder:
           return await update_order(order, existingOrder)    
    return await create_new_order(user, order)  
 
 
async def create_new_order(user: UserForAddress, order: Order):
    code = str(uuid4())
   
    order_data = dict(
        user = user.dict(),
        order = [ {code: order.dict() }]
       
        )
 
    # order = await order_collection.insert_one(dict(order_data))
    # if order.inserted_id:
       
    #     order = await get_order_id(code)
    #     return order
 
async def  update_order(order: Order, existingOrder):
    try:    
        #TODO validar se o endereco ja existe          
        code = str(uuid4())
        order = await order_collection.update_one(
            {'_id': existingOrder['_id']},
            {"$addToSet": {"order":{code: order.dict() } }}      
           
        )
        if order.modified_count:
            return order.modified_count
 
        return None
    except Exception as e:
        print(f'update_order.error: {e}')  
 
async def get_order_user_code(user_code):
    try:      
        data = await order_collection.find_one({"user": {"email" : user_code }})
        if data:
            print(data)
            return data
 
    except Exception as e:
        print(f"get_order_id.error: {e}")
 
 
# Retorna o endereço pelo code do usuário
async def get_order_by_user_email(user_email):
   
    data = await order_collection.find_one({"user": {"email": user_email}})
    print(data)
    if data:
        return data
    else:
        return "droga!"
 
# async def get_all() -> List[dict]:
#     filter = {}
#     cursor_pesquisa = order_collection.find(filter)
#     list_all = [order async for order in cursor_pesquisa]
#     return list_all
 
 
# # Deleta o endereço
# async def delete_order(order_collection, order_code):
#     try:
#         order = await order_collection.delete_one(
#             {"_code": order_code}
#         )
#         if order.deleted_count:
#             return {"status": "Endereço deletado"}
 
#     except Exception as e:
#         print(f'delete_order.error: {e}')
 
# Retorna os endereços
async def get_user_order(skip, limit):
    user_cursor = order_collection.find().skip(int(skip)).limit(int(limit))
    order = await user_cursor.to_list(length=int(limit))
    return order
 
 
 

