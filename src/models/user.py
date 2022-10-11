from typing import Optional, List
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

class User(BaseModel):
    name: str = Field(...,min_length=5, max_length=128, description= "Nome do usuário")
    email: EmailStr = Field(unique=True, index=True)
    password: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    
class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    is_active: Optional[bool]
    is_admin: Optional[bool]
    
class UserCode(BaseModel):
    code: str = Field(..., description="Código do usuário, no formato uuid v4")
   
class UserGeneral(UserCode, User):
    ...

class UserForAddress(BaseModel):
    user_code: str
    email: EmailStr
    
 




