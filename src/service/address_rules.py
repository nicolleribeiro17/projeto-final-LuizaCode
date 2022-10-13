from typing import List, Optional
from uuid import uuid4
from models.order import OrderGeneral
from models.user import UserForAddress

from server import address_server
from models.address import Address, AddressGeneral

from service.rules_exception import ExceptionNotFound, OtherCodesExceptions

CAMPO_CODE = address_server.AddressField.CODE


# Cria endereço para o usuario
async def create_address(user: UserForAddress, address: Address):   
    existingAddress = await search_by_user_code(user.user_code)
    print(existingAddress)
    if existingAddress:
           return await insert_new_address(address, existingAddress)     
    return await create_new_address(user, address)  


#Cria um endereco quando o usuario ainda nao tem nenhum cadastrado
async def create_new_address(user: UserForAddress, address: Address):
    new_address = address.dict()
    new_address["code"] = str(uuid4())    
    address_data ={ 'user' : user.dict(), 'address' : [new_address], 'code' :str(uuid4()) }
    address = await address_server.create_address_user(address_data)     
    return {'code': new_address['code'] }

#Insere mais um endereco para o mesmo usuario
async def  insert_new_address(address: Address, existingAddress: Address):      
    #TODO validar se o endereco ja existe          
    new_address = address.dict()
    new_address["code"] = str(uuid4())
    address = await address_server.insert_new_address(new_address,existingAddress)
    return {'code': new_address['code'] }   


# procura o endereço pelo codigo do usuário
async def search_by_user_code(code: str) -> Optional[dict]:
    address = await address_server.get_address_user_id(code)    
    return address

# procura o endereço pelo codigo do endereco
async def search_by_address_code(code: str):
    address = await address_server.get_address_by_address_id(code)
    return address

# procura o endereço pelo email do usuário
async def get_address_by_user_email(code: str) -> Optional[dict]:
    return await address_server.get_address_by_user_email(code)

# busca o endereco principal
async def get_delivery_address(code: str) -> Optional[dict]:
   #TODO get delivery address
   address = None
   if not address:
      raise ExceptionNotFound("Endereco não encontrada")

# busca o endereço para entrega baseado no valor passado na order  
async def get_user_address_order(order: OrderGeneral):
    if order.address:
        if order.address.address:
            return  order.address.address
        if order.address.address_code:
            return  search_by_user_code(order.user.code)   
    return await get_delivery_address(order.user.code)




