from typing import List, Optional
from uuid import uuid4
from models.user import UserForAddress

from server import address_server
from models.address import Address, AddressGeneral

from service.rules_exception import ExceptionNotFound, OtherCodesExceptions

CAMPO_CODE = address_server.AddressField.CODE


# Cria endereço associado ao usuario
async def create_address(user: UserForAddress, address: Address):   
    existingAddress = await search_by_user_code(user.user_code)
    if existingAddress:
           return await insert_new_address(address, existingAddress)     
    return await create_new_address(user, address)  


#Cria um endereco para o usuario
async def create_new_address(user: UserForAddress, address: Address):
    code = str(uuid4())
    
    address_data = dict(user = user.dict(), address = [ {code: address.dict() }] )
    address = await address_server.create_address_user(dict(address_data))     
    return {'code': code }

#Insere mais um endereco para o mesmo usuario
async def  insert_new_address(address: Address, existingAddress: Address):
      
    #TODO validar se o endereco ja existe          
    code = str(uuid4()) 
    address = await address_server.insert_new_address(address,existingAddress,code)
    return {'code': code }   


# procura o endereço pelo codigo do usuário
async def search_by_user_code(code: str) -> Optional[dict]:
    address = await address_server.get_address_user_id(code)
    return address


async def get_address_by_user_email(code: str) -> Optional[dict]:
    return await address_server.get_address_by_user_email(code)
  


# async def remove_by_code(code: str):
#     remove = await address_server.delete_by_code(code)

#     if not remove:
#         raise ExceptionNotFound("Usuário não encontrada")


