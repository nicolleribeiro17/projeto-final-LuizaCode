"""
Regras e ajustes para Produtos.
"""

from typing import List, Optional
from uuid import uuid4

import server.product_server as product_server
from models.product import Product, ProductGeneral, ProductUpdated
from service.rules_exception import OtherExceptionRules, RulesException, ExceptionNotFound, OtherCodesExceptions

CAMPO_CODE = product_server.ProductField.CODE

# procura o produto pelo codigo
async def search_by_code(code: str, throws_exception_if_not_found: bool = False) -> Optional[dict]:
    product = await product_server.get_by_code(code)
    if not product and throws_exception_if_not_found:
        raise ExceptionNotFound("Produto não encontrado")
    return product

# procura o produto pelo sku
async def search_by_sku(sku: str, throws_exception_if_not_found: bool = False) -> Optional[dict]:
    product_sku = await product_server.get_by_sku(sku)
    if not product_sku and throws_exception_if_not_found:
        raise ExceptionNotFound("Produto não encontrado")
    return product_sku

# procura pelo nome
async def search_by_name(name: str, lanca_excecao_se_nao_encontrado: bool = False) -> Optional[dict]:
    product = await product_server.get_by_name(name)
    if not product and lanca_excecao_se_nao_encontrado:
        raise ExceptionNotFound("Produto não encontrado")
    return product

# procura pela categoria
async def search_by_category(category: str, lanca_excecao_se_nao_encontrado: bool = False) -> Optional[dict]:
    product = await product_server.get_by_category(category)
    if not product and lanca_excecao_se_nao_encontrado:
        raise ExceptionNotFound("Produto não encontrado")
    return product

# busca todos 
async def search_all() -> List[dict]:
    all = await product_server.get_all()
    return all

# valida o produto
async def validate_product(product: Product, code_base: Optional[str] = None):
    is_new_product = code_base is None

    other_product = await product_server.get_by_sku(product.sku)
    if (other_product is not None) and (
        is_new_product or
        (code_base != other_product[CAMPO_CODE])
    ):
        raise OtherExceptionRules("Há outro produto com este sku")


async def insert_new_product(product: Product) -> ProductGeneral:
    await validate_product(product)
    new_product = product.dict()
    new_product[product_server.ProductField.CODE] = str(uuid4())
    await product_server.create_new_product(new_product)
    product_geral = ProductGeneral(**new_product)
    return product_geral

async def remove_by_code(code: str):
    remove = await product_server.delete_by_code(code)

    if not remove:
        raise ExceptionNotFound("Usuário não encontrada")

async def update_by_code(code: str, product: ProductUpdated):

    await search_by_code(code, True)

    data = dict(product)
    data = {k: v for k, v in data.items() if v is not None}

    await product_server.update_product_by_code(
        code, data
    )