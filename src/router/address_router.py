from typing import List

from pydantic import BaseModel, Field

#import service.address_rules as address_rules
from fastapi import APIRouter, status
from models.address import AddressCode, Address, AddressGeneral
from server.address_server import create_address_user, get_address_by_user_code

# Minha rota API de endereços
address_route = APIRouter(prefix="/api/addresss",tags=["addresss"],)

ADDRESS_CREATION_DESCRIPTION = """
Criação de um novo endereço. Para registrar um novo endereço:

- `nome` Deve ter no minimo 10 caracteres.
- `email`: Deve ter nome único.
- `password`: Deve ter uma senha.
- `tempo`: Opcionalmente pode ter um tempo. Se informado deve ser
maior que 0 (zero).

Se o endereço for criado corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`codigo`, que é o código do novo endereço em nosso sistema.
"""


@address_route.post("/", summary="Criação de novo endereço",description=ADDRESS_CREATION_DESCRIPTION, status_code=status.HTTP_201_CREATED, response_model = AddressCode)

async def create_new_address(address: Address):
    new_address = await create_address_user(address)
    return new_address


# @address_route.put("/{codigo}",status_code=status.HTTP_202_ACCEPTED,
#     summary="Atualização do endereço",
#     description="Atualiza um endereço pelo código",)
# async def update_address(code: str, address: AddressUpdate):
#     await address_rules.update_by_code(code, address)


# @address_route.delete("/{code}", status_code=status.HTTP_202_ACCEPTED, summary="Remoção do endereço",
#     description="Remove o endereço pelo código",)
# async def remove_address(code: str):
#     await address_rules.remove_by_code(code)


@address_route.get("/{code}",response_model=AddressGeneral,summary="Pesquisar pelo endereço",
    description="Pesquisar um endereço pelo código",)
async def get_address_by_code(code: str):
    address = await get_address_by_user_code(code, True)
    return address


# @address_route.get("/",response_model=List[AddressGeneral],
#     summary="Pesquisar todos os endereços",
#     description="Pesquisar por todos os endereços.",)

# async def get_all_addresss() -> List[AddressGeneral]:
#     all = await address_rules.search_all()
#     return all
