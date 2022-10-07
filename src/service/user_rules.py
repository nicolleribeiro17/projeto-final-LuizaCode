"""
Regras e ajustes para Usuários.
"""

from typing import List, Optional
from uuid import uuid4

from server import user_server
from models.user import User, UserGeneral

from service.rules_exception import OtherExceptionRules, RulesException, ExceptionNotFound, OtherCodesExceptions

CAMPO_CODE = user_server.UserField.CODE

# procura o usuário pelo codigo
async def search_by_code(code: str, throws_exception_if_not_found: bool = False) -> Optional[dict]:
    user = await user_server.get_by_code(code)
    if not user and throws_exception_if_not_found:
        raise ExceptionNotFound("Usuário não encontrado")
    return user

async def search_by_email(email: str, throws_exception_if_not_found: bool = False) -> Optional[dict]:
    user_mail = await user_server.get_by_email(email)
    if not user_mail and throws_exception_if_not_found:
        raise ExceptionNotFound("Usuário não encontrado")
    return user_mail

# busca todos 
async def search_all() -> List[dict]:
    all = await user_server.get_all()
    return all


async def validate_user(user: User, code_base: Optional[str] = None):
    is_new_user = code_base is None
      
    other_user = await user_server.get_by_email(user.email)
    if (other_user is not None) and (
        is_new_user or
        (code_base != other_user[CAMPO_CODE])
    ):
        raise OtherExceptionRules("Há outro usuário com este email")


async def insert_new_user(user: User) -> UserGeneral:
    await validate_user(user)

    new_user = user.dict()
    new_user[user_server.UserField.CODE] = str(uuid4())
    await user_server.create_new_user(new_user)
    user_geral = UserGeneral(**new_user)
    return user_geral


async def remove_by_code(code: str):
    remove = await user_server.delete_by_code(code)

    if not remove:
        raise ExceptionNotFound("Usuário não encontrada")


async def update_by_code(code: str, user: UserGeneral):
    await search_by_code(code, True)

    if user.code is not None and user.code != code:
        raise OtherCodesExceptions
    validate_user(user, code)

    user_for_database = user.dict()

    if user.code is None:
        user_for_database.pop(CAMPO_CODE, None)

    await user_server.update_user_by_code(
        code, user_for_database
    )
