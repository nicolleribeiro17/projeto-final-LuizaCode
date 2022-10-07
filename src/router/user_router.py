from typing import List

from pydantic import BaseModel, Field

import service.user_rules as user_rules
from fastapi import APIRouter, status
from models.user import User, UserCode, UserGeneral, UserUpdate

# Minha rota API de Usuários
user_route = APIRouter(prefix="/api/users",tags=["Users"],)

USER_CREATION_DESCRIPTION = """
Criação de um novo usuário. Para registrar um novo usuário:

- `nome` Deve ter no minimo 10 caracteres.
- `email`: Deve ter nome único.
- `password`: Deve ter uma senha.
- `tempo`: Opcionalmente pode ter um tempo. Se informado deve ser
maior que 0 (zero).

Se o usuário for criado corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`codigo`, que é o código do novo usuário em nosso sistema.
"""

# Colocamos este modelo aqui, SOMENTE para ficar perto da documentação.
# Seria apropriado criar um 'modelo' para cada erro??

class HasAnotherEmail(BaseModel):
    """
    Outro usuário possui o mesmo email que o usuário corrente.
    """
    message: str = Field(..., description="Mensagem com a causa do problema")

    class Config:
        schema_extra = {
            "example": {
            "message": "Há outro usuário com este email",
            }}


@user_route.post("/", summary="Criação de novo usuário",description=USER_CREATION_DESCRIPTION, status_code=status.HTTP_201_CREATED, response_model = UserCode,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Já temos outro usuário com este email.",
            "model": HasAnotherEmail
        }
    },
)

async def create_new_user(user: User):
    new_user = await user_rules.insert_new_user(user)
    return new_user


@user_route.put("/{codigo}",status_code=status.HTTP_202_ACCEPTED,
    summary="Atualização do usuário",
    description="Atualiza um usuário pelo código",
)
async def update_user(code: str, user: UserUpdate):
    await user_rules.update_by_code(code, user)


@user_route.delete("/{code}", status_code=status.HTTP_202_ACCEPTED, summary="Remoção do usuário",
    description="Remove o usuário pelo código",)

async def remove_user(code: str):
    await user_rules.remove_by_code(code)


@user_route.get("/{code}",response_model=UserGeneral,summary="Pesquisar pelo usuário",
    description="Pesquisar um usuário pelo código",)
async def get_user_by_code(code: str):
    user = await user_rules.search_by_code(code, True)
    return user


@user_route.get("/",response_model=List[UserGeneral],
    summary="Pesquisar todos os usuários",
    description="Pesquisar por todos os usuários.",)

async def get_all_users() -> List[UserGeneral]:
    all = await user_rules.search_all()
    return all
