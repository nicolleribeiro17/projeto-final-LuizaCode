from fastapi import APIRouter, status
 
from models.address import Address
from models.user import User, UserCode, UserForAddress
from service.address_rules import create_address,get_address_by_user_email
from description.address_description import CreationDescription, EmailDescription
 
address_route = APIRouter(prefix="/api/address",tags=["address"],)
 
@address_route.post("/", summary="Criação de novo endereço",
    description=CreationDescription.ADDRESS_CREATION_DESCRIPTION, status_code=status.HTTP_201_CREATED)
async def create_new_address(user: UserForAddress, address: Address):
    new_address = await create_address(user,address)
    return new_address
 
 
@address_route.get("/email/{email}", summary="Pesquisar pelo endereço",
    description=EmailDescription.GET_USER_EMAIL_DESCRIPTION, status_code=status.HTTP_200_OK)
async def get_address_by_code(email: str):
    address = await get_address_by_user_email(email)
    return address
 


