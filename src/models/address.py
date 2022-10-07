from typing import Optional, List
from pydantic import BaseModel, Field
from models.user import User


class Address(BaseModel):
    street: str = Field(None,min_lenght = 3, max_lenght = 100)
    zip_code: str = Field(None,min_lenght = 8, max_lenght = 9)
    district: str = Field(None,min_lenght = 3, max_lenght = 100)
    city: str = Field(None,min_lenght = 3, max_lenght = 100)
    state: str = Field(None,min_lenght = 2, max_lenght =2)
        
class AddressCode(BaseModel):
    code: str = Field(..., description="Código do usuário, no formato uuid v4",)
     
    class Config:
        schema_extra = {
            "example": {
                "codigo": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6",
            }
        }


class AddressUpdate(BaseModel):
    street: Optional[str]
    zip_code: Optional[str]
    district: Optional[str]
    city: Optional[str]
    state: Optional[str]
    is_delivery: Optional[bool]

class AddressList(Address):
    _id: str
    user: User
    
    class Config:
        orm_mode = True

class AddressGeneral(AddressCode, Address):
    ...

class UserAddress(BaseModel):
    user: User
    address: List[Address] = []