from bson.json_util import dumps
import json
from models.address import Address
from .database import get_collection


address_collection = get_collection("address")

class AddressField:
    CODE = "code"
    

async def create_address_user(address: dict):  
    try:  
        address = await address_collection.insert_one(address)
        return  address  
    except Exception as e:
        print(f'create_address_user.error: {e}')  
    

async def  insert_new_address(address: Address, existingAddress: Address):
    try:  
        address = await address_collection.update_one(
            {'_id': existingAddress['_id']},
            {"$addToSet": {"address":address }}       
            
        ) 
        if address.modified_count:
            return address.modified_count 
        return None
    except Exception as e:
        print(f'insert_new_address.error: {e}')  


async def get_address_user_id(code):
    try:        
        data = await address_collection.find_one({"user.user_code" : code})
        if data:           
            return data
    except Exception as e:
        print(f"get_address_id.error: {e}")


async def get_address_by_address_id(code):
    try:        
        data = await address_collection.find_one({"address.code" : code})
        if data:           
            return data
    except Exception as e:
        print(f"get_address_id.error: {e}")


async def get_address_by_user_email(user_email):
    try: 
        data = await address_collection.find_one({"user.email": user_email})
        if data:
            return json.loads(dumps(data["address"]))
    except Exception as e:
        print(f"get_address_by_user_email.error: {e}")

async def get_delivery_address(filter: dict):
    try:        
        data = await address_collection.find_one(filter)
        if data:           
            return data
    except Exception as e:
        print(f"get_address_id.error: {e}")    





