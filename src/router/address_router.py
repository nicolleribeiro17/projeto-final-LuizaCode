from typing import List

from pydantic import BaseModel, Field

#import service.address_rules as address_rules
from fastapi import APIRouter, status
from models.address import Address, AddressGeneral, UserAddress
from models.user import User, UserCode, UserForAddress
from service.address_rules import create_address,get_address_by_user_email

# Minha rota API de endereços
address_route = APIRouter(prefix="/api/address",tags=["address"],)

ADDRESS_CREATION_DESCRIPTION = """
Criação de um novo endereço para o usuario:

- `street` Rua
- `number` Numero
- `zip_code`: CEP.
- `district`: Bairro.
- `city`: Cidade.
- `state`: Estado (Apenas a sigla).
- `is_delivery`: E endereco padrao para entrega.


Se o endereço for criado corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`codigo`, que é o código do novo endereço em nosso sistema.
"""


@address_route.post("/", summary="Criação de novo endereço",
    description=ADDRESS_CREATION_DESCRIPTION, status_code=status.HTTP_200_OK)
async def create_new_address(user: UserForAddress, address: Address):
    new_address = await create_address(user,address)
    return new_address


@address_route.get("/email/{email}", summary="Pesquisar pelo endereço",
    description="Pesquisar um endereço pelo código",)
async def get_address_by_code(email: str):
    address = await get_address_by_user_email(email)
    return address





