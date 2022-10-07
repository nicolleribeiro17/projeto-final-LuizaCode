from typing import List

from pydantic import BaseModel, Field

import service.user_rules as user_rules
from fastapi import APIRouter, status
from models.user import User, UserList, UserCode, UserGeneral, UserUpdate

# Minha rota API de Usuários
rota_usuario = APIRouter(prefix="/api/users",tags=["Usuários"],)

USER_CREATION_DESCRIPTION = """
Criação de um novo usuário. Para registrar uma nova usuário:

- `nome`: Deve ter nome único.
- `artista`: Deve ter uma pessoa artista.
- `tempo`: Opcionalmente pode ter um tempo. Se informado deve ser
maior que 0 (zero).

Se a usuário for criada corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`codigo`, que é o código da nova usuário em nosso sistema.
"""

# Colocamos este modelo aqui, SOMENTE para ficar perto da documentação.
# Seria apropriado criar um 'modelo' para cada erro??

class HasAnotherEmail(BaseModel):
    """
    Outro usuário possui o mesmo nome que a usuário corrente.
    """
    message: str = Field(..., description="Mensagem com a causa do problema")

    class Config:
        schema_extra = {
            "example": {
            "message": "Há outro usuário com este nome",
            }}


@rota_usuario.post("/", summary="Criação de novo usuário",description=USER_CREATION_DESCRIPTION,
    status_code=status.HTTP_201_CREATED, response_model = UserCode,
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


@rota_usuario.put("/{codigo}",status_code=status.HTTP_202_ACCEPTED,
    summary="Atualização do usuário",
    description="Atualiza um usuário pelo código",
)
async def update_user(code: str, user: UserUpdate):
    await user_rules.update_by_code(code, user)


@rota_usuario.delete("/{code}", status_code=status.HTTP_202_ACCEPTED, summary="Remoção do usuário",
    description="Remove o usuário pelo código",)

async def remove_user(code: str):
    # Remove uma usuário pelo código
    await user_rules.remove_by_code(code)


@rota_usuario.get("/{code}",response_model=UserGeneral,summary="Pesquisar pelo usuário",
    description="Pesquisar um usuário pelo código",)
async def get_user_by_code(code: str):
    # Pesquisa a usuário pelo código.
    user = await user_rules.search_by_code(code, True)
    return user


@rota_usuario.get("/",response_model=List[UserGeneral],
    summary="Pesquisar todos os Usuários",
    description="Pesquisar por todos os Usuários.",)

async def get_all_users() -> List[UserGeneral]:
    # Pesquisar por todos as Usuários (sem um filtro)
    all = await user_rules.search_all()
    return all
