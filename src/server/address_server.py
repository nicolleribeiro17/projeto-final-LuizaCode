from bson.json_util import dumps
import json
from models.address import Address
from .database import get_collection


address_collection = get_collection("address")

class AddressField:
    CODE = "code"
    

# Cria endereço associado ao usuario
async def create_address_user(address: dict):  
    try:  
        address = await address_collection.insert_one(dict(address))
        return  address  
    except Exception as e:
        print(f'create_address_user.error: {e}')  
    
     
#Insere mais um endereco para um usuario
async def  insert_new_address(address: Address, existingAddress: Address, code):
    try:  
        address = await address_collection.update_one(
            {'_id': existingAddress['_id']},
            {"$addToSet": {"address":{code: address.dict() } }}       
            
        ) 
        if address.modified_count:
            return address.modified_count 
        return None
    except Exception as e:
        print(f'insert_new_address.error: {e}')  

# Retorna o endereço pelo code do usuário
async def get_address_user_id(code):
    try:        
        data = await address_collection.find_one({"user.user_code" : code})
        if data:           
            return data
    except Exception as e:
        print(f"get_address_id.error: {e}")


# Retorna uma lista de endereço pelo e-mail do usuário
async def get_address_by_user_email(user_email):
    try: 
        data = await address_collection.find_one({"user.email": user_email})
        if data:
            return json.loads(dumps(data["address"]))
    except Exception as e:
        print(f"get_address_by_user_email.error: {e}")
    


# # Deleta o endereço
# async def delete_address(address_collection, address_code):
#     try:
#         address = await address_collection.delete_one(
#             {"_code": address_code}
#         )
#         if address.deleted_count:
#             return {"status": "Endereço deletado"}

#     except Exception as e:
#         print(f'delete_address.error: {e}')

