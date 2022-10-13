from email.policy import default
from typing import Optional, List
from pydantic import BaseModel, Field
from models.user import  UserForAddress


class Address(BaseModel):
    street: str = Field(None,min_lenght = 3, max_lenght = 100)
    number: int = Field(None,min_lenght = 1, max_lenght = 5)
    zip_code: str = Field(None,min_lenght = 8, max_lenght = 9)
    district: str = Field(None,min_lenght = 3, max_lenght = 100)
    city: str = Field(None,min_lenght = 3, max_lenght = 100)
    state: str = Field(None,min_lenght = 2, max_lenght =2)
    is_delivery: bool = Field(default = False)
 
        
class AddressCode(BaseModel):
    code: str = Field(..., description="Código do usuário, no formato uuid v4")
        

class AddressUpdate(BaseModel):
    street: Optional[str]
    number: Optional[int]
    zip_code: Optional[str]
    district: Optional[str]    
    city: Optional[str]
    state: Optional[str]
    is_delivery: Optional[bool]


class AddressGeneral(BaseModel):
    address_code: AddressCode
    address:Address

class UserAddress(BaseModel):
    user: UserForAddress
    address: List[Address] = []


class orderAddress(BaseModel):
    address_code: Optional[str]
    address: Optional[Address] 
    

