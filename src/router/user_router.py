from typing import List
 
import service.user_rules as user_rules
from fastapi import APIRouter, status
from models.user import User, UserCode, UserGeneral, UserUpdate
from router.error import HasAnotherEmail
from description.user_description import (
     CreationDescription, CodeDescription, DeleteDescription, EmailDescription, UpdateDescription, UserDescription
    )
 
user_route = APIRouter(prefix="/api/users",tags=["Users"],)
 
@user_route.post("/", summary="Criação de novo usuário",description=CreationDescription.USER_CREATION_DESCRIPTION, status_code=status.HTTP_201_CREATED, response_model = UserCode,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Já existe outro usuário com este email.",
            "model": HasAnotherEmail
        }
    },
)
 
async def create_new_user(user: User):
    new_user = await user_rules.create_new_user(user)
    return new_user
 

@user_route.put("/update/{code}",status_code=status.HTTP_200_OK,
    summary="Atualização do usuário",
    description=UpdateDescription.USER_UPDATE_DESCRIPTION,
)
async def update_user(code: str, user: UserUpdate):
    await user_rules.update_by_code(code, user)
 

@user_route.delete("/delete/{code}", status_code=status.HTTP_200_OK, summary="Remoção do usuário",
    description=DeleteDescription.USER_DELETE_DESCRIPTION,)
 
async def remove_user(code: str):
    await user_rules.remove_by_code(code)
 

@user_route.get("/code/{code}",response_model=UserGeneral,status_code=status.HTTP_200_OK,summary="Pesquisar pelo usuário",
    description=CodeDescription.GET_USER_CODE_DESCRIPTION)
async def get_user_by_code(code: str):
    user = await user_rules.search_by_code(code, True)
    return user
 

@user_route.get("/",response_model=List[UserGeneral], status_code=status.HTTP_200_OK,
    summary="Pesquisar todos os usuários", description=UserDescription.GET_ALL_DESCRIPTION,)
 
async def get_all_users() -> List[UserGeneral]:
   
    all = await user_rules.search_all()
    return all
 

@user_route.get("/email/{email}",response_model=UserGeneral,status_code=status.HTTP_200_OK,
summary="Pesquisar pelo usuário", description=EmailDescription.GET_USER_EMAIL_DESCRIPTION)
async def get_user_by_code(email: str):
   
    user = await user_rules.search_by_email(email, True)
    return user
 
