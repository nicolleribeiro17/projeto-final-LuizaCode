"""
Módulo responsável pela persistência das músicas.
Este conversa com Mongo para inserir, atualizar, remover
e pesquisar as músicas no MongoDB.
"""

from typing import List, Optional

from .database import get_collection


class ProductField:
    CODE = "code"
    NAME = "name"


product_collection = get_collection("product")

async def get_by_code(product_code: str) -> Optional[dict]:
    filter = {
        ProductField.CODE: product_code
    }
    product = await product_collection.find_one(filter)
    return product


async def get_all() -> List[dict]:
    filter = {}
    cursor_pesquisa = product_collection.find(filter)
    list_all = [
        product
        async for product in cursor_pesquisa
    ]
    return list_all


async def get_by_name(name: str) -> Optional[dict]:
    filter = {
        ProductField.NAME: name
    }
    product = await product_collection.find_one(filter)

    return product


async def create_new_product(new_product: dict) -> dict:
    await product_collection.insert_one(new_product)
    return new_product


async def delete_by_code(product_code: str) -> bool:

    filter = {ProductField.CODE: product_code}
    result = await product_collection.delete_one(filter)
    removed = result.deleted_count > 0
    return removed

async def update_product_by_code(product_code: str, product: dict) -> bool:
    filter = {
        ProductField.CODE: product_code
    }
    update_register = {
        "$set": product
    }
    response = await product_collection.update_one(filter, update_register)
    return response.modified_count == 1