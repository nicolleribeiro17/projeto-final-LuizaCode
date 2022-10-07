from bson import ObjectId
from bson.objectid import ObjectId

from .database import get_collection


address_collection = get_collection("address")

# Cria endereço associado ao usuario
async def create_address_user(user, address):
    address_data = dict(
        user = user,
        address = [address]
        )

    address = await address_collection.insert_one(dict(address_data))
    if address.inserted_id:
        address = await (address.inserted_id, address_collection, 'address')
        return address


# Retorna o endereço pelo code do usuário
async def get_address_by_user_code(user_code):
    data = await address_collection.find_one({"user._code": ObjectId(user_code)})
        
    if data:
        return data



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

# Retorna os endereços 
async def get_user_address(skip, limit):
    user_cursor = address_collection.find().skip(int(skip)).limit(int(limit))
    address = await user_cursor.to_list(length=int(limit))
    return address
