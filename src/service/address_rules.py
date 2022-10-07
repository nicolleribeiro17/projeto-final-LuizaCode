from typing import List, Optional
from uuid import uuid4

from server import address_server
from models.address import Address, AddressGeneral

from service.rules_exception import OtherExceptionRules, RulesException, ExceptionNotFound, OtherCodesExceptions

CAMPO_CODE = address_server.AddressField.CODE

# procura o endereço pelo codigo do usuário
async def search_by_code(code: str, throws_exception_if_not_found: bool = False) -> Optional[dict]:
    address = await address_server.get_by_code(code)
    if not address and throws_exception_if_not_found:
        raise ExceptionNotFound("Usuário não encontrado")
    return address

# busca todos 
async def search_all() -> List[dict]:
    all = await address_server.get_all()
    return all


# async def validate_address(address: Address, code_base: Optional[str] = None):
#     is_new_address = code_base is None
      
#     other_address = await address_server.get_by_code(address.code)
#     if (other_address is not None) and (
#         is_new_address or
#         (code_base != other_address[CAMPO_CODE])
#     ):
#         raise OtherExceptionRules("Há outro usuário com este código")


async def insert_new_address(address: Address) -> AddressGeneral:

    new_address = address.dict()
    new_address[address_server.AddressField.CODE] = str(uuid4())
    await address_server.create_new_address(new_address)
    address_geral = AddressGeneral(**new_address)
    return address_geral


async def remove_by_code(code: str):
    remove = await address_server.delete_by_code(code)

    if not remove:
        raise ExceptionNotFound("Usuário não encontrada")


async def update_by_code(code: str, address: AddressGeneral):
    await search_by_code(code, True)

    if address.code is not None and address.code != code:
        raise OtherCodesExceptions
    # validate_address(address, code)

    address_for_database = address.dict()

    if address.code is None:
        address_for_database.pop(CAMPO_CODE, None)

    await address_server.update_address_by_code(
        code, address_for_database
    )
