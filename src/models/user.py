from typing import Optional, List
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

class User(BaseModel):
    name: str = Field(...,min_length=5, max_length=128, description= "Nome do usuário")
    email: EmailStr = Field(unique=True, index=True)
    password: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=True)
    
class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    is_active: Optional[bool]
    is_admin: Optional[bool]
    
class UserCode(BaseModel):
    code: str = Field(..., description="Código do usuário, no formato uuid v4",)
     
    class Config:
        schema_extra = {
            "example": {
                "codigo": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6",
            }
        }

class UserGeneral(UserCode, User):
    ...

class UserList(User):
    _id: str
    email: EmailStr
    
    class Config:
        orm_mode = True




