"""
Regras e ajustes para Produtos.
"""

from typing import List, Optional
from uuid import uuid4

from server import product_server
from models.product import Product, ProductGeneral

from service.rules_exception import OtherExceptionRules, RulesException, ExceptionNotFound, OtherCodesExceptions



CAMPO_CODE = product_server.ProductField.CODE

# procura pelo codigo
async def search_by_code(code: str, lanca_excecao_se_nao_encontrado: bool = False) -> Optional[dict]:
    product = await product_server.get_by_code(code)
    if not product and lanca_excecao_se_nao_encontrado:
        raise ExceptionNotFound("Produto não encontrado")
    return product


async def search_all() -> List[dict]:
    todas = await product_server.get_all()
    return todas

async def validate_product(product: Product, code_base: Optional[str] = None):
    is_new_product = code_base is None
      
    outra_product = await product_server.get_by_name(product.name)
    if (outra_product is not None) and (
        is_new_product or
        (code_base != outra_product[CAMPO_CODE])
    ):
        raise OtherExceptionRules("Há outra Produto com este nome")


async def insert_new_product(product: Product) -> ProductGeneral:
    await validate_product(product)

    novo_product = product.dict()
    novo_product[product_server.ProductField.CODE] = str(uuid4())

    await product_server.create_new_product(novo_product)

    product_geral = ProductGeneral(**novo_product)

    return product_geral


async def remove_by_code(code: str):
    removeu = await product_server.delete_by_code(code)

    if not removeu:
        raise ExceptionNotFound("Produto não encontrada")


async def update_by_code(code: str, product: ProductGeneral):
    await search_by_code(code, True)

    if product.code is not None and product.code != code:
        raise OtherCodesExceptions
    validate_product(product, code)

    product_para_banco = product.dict()

    if product.code is None:
        product_para_banco.pop(CAMPO_CODE, None)

    await product_server.update_product_by_code(
        code, product_para_banco
    )
