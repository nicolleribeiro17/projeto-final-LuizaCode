

"""
Módulo responsável pela persistência das músicas.
Este conversa com Mongo para inserir, atualizar, remover
e pesquisar as músicas no MongoDB.
"""

from typing import List, Optional

from .database import get_collection


class UserField:
    CODE = "code"
    EMAIL = "email"


user_collection = get_collection("user")

async def get_by_code(user_code: str) -> Optional[dict]:
    try:
        filter = { UserField.CODE: user_code }
        user = await user_collection.find_one(filter)
        return user
    except Exception as e:
        print(f'get_by_code.error: {e}') 

async def get_all() -> List[dict]:
    try:
        filter = {}
        cursor_pesquisa = user_collection.find(filter)
        list_all = [user async for user in cursor_pesquisa]
        return list_all
    except Exception as e:
        print(f'get_all.error: {e}') 

async def get_by_email(email: str) -> Optional[dict]:
    try:
        filter = { UserField.EMAIL: email }
        user = await user_collection.find_one(filter)
        return user
    except Exception as e:
        print(f'get_by_email.error: {e}') 

async def create_new_user(new_user: dict) -> dict:
    try:
        await user_collection.insert_one(new_user)
        return new_user
    except Exception as e:
        print(f'create_new_user.error: {e}')

async def delete_by_code(user_code: str) -> bool:
    try:
        filter = {UserField.CODE: user_code}
        result = await user_collection.delete_one(filter)
        removed = result.deleted_count > 0
        return removed
    except Exception as e:
        print(f'delete_by_code.error: {e}')

async def update_user_by_code(user_code: str, user: dict) -> bool:
    try:
        filter = { UserField.CODE: user_code }
        update_register = {
            "$set": user
        }
        response = await user_collection.update_one(filter, update_register)
        return response.modified_count == 1
    except Exception as e:
        print(f'update_user_by_code.error: {e}')
