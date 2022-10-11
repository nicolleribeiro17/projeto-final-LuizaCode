"""
Módulo responsável pela persistência dos produtos.
Este conversa com Mongo para inserir, atualizar, remover
e pesquisar os produtos no MongoDB.
"""

from typing import List, Optional

from .database import get_collection


class ProductField:
    CODE = "code"
    SKU = "sku"
    NAME = "name"
    CATEGORY = "category"
product_collection = get_collection("product")

# procura pelo SKU
async def get_by_sku(product_sku: str) -> Optional[dict]:
    filter = { ProductField.SKU: product_sku }
    product = await product_collection.find_one(filter)
    return product

# procura pelo código
async def get_by_code(product_code: str) -> Optional[dict]:
    filter = { ProductField.CODE: product_code }
    product = await product_collection.find_one(filter)
    return product

# procura pelo nome
async def get_by_name(product_name: str) -> Optional[dict]:
   
    filter = {
        ProductField.NAME: product_name
    }
    cursor_pesquisa = product_collection.find(filter)
    print(cursor_pesquisa)
    list_all = [
        product
        async for product in cursor_pesquisa
    ]
    return list_all

# procura pela categoria
async def get_by_category(product_category: str) -> Optional[dict]:
   
    filter = {
        ProductField.CATEGORY: product_category
    }
    cursor_pesquisa = product_collection.find(filter)
    print(cursor_pesquisa)
    list_all = [
        product
        async for product in cursor_pesquisa
    ]
    return list_all

# procuta todos os produtos
async def get_all() -> List[dict]:
    filter = {}
    cursor_pesquisa = product_collection.find(filter)
    list_all = [product async for product in cursor_pesquisa]
    return list_all

# cria produto
async def create_new_product(new_product: dict) -> dict:
    try:
        await product_collection.insert_one(new_product)
        return new_product
    except Exception as e:
        print(f'create_new_product.error: {e}')  


# deleta produto pelo codigo
async def delete_by_code(product_code: str) -> bool:
    filter = {ProductField.CODE: product_code}
    result = await product_collection.delete_one(filter)
    removed = result.deleted_count > 0
    return removed

async def update_product_by_code(product_code: str, product: dict) -> bool:
    filter = { ProductField.CODE: product_code }
    update_register = {
        "$set": product
    }
    response = await product_collection.update_one(filter, update_register)
    return response.modified_count == 1