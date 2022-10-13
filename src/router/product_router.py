from typing import List
from fastapi import APIRouter, status
 
import service.product_rules as product_rules
from models.product import Product, ProductGeneral, ProductUpdated, ProductCode
from router.error import HasAnotherSku
from description.product_description import (
    CreationDescription, CategoryDescription, CodeDescription, DeleteDescription, SkuDescription, NameDescription, UpdateDescription, ProductDescription
    )
 
 
product_route = APIRouter(prefix="/api/products",tags=["Products"],)
 

@product_route.post("/", summary="Criação de novo Produto",description=CreationDescription.PRODUCT_CREATION_DESCRIPTION,
    status_code=status.HTTP_201_CREATED, response_model = ProductCode,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Já temos outro produto com este sku.",
            "model": HasAnotherSku
        }
    },
)
async def create_new_product(product: Product):
    print(product)
    new_product = await product_rules.crate_new_product(product)
    return new_product
 

@product_route.put("/update/code/{code}",status_code=status.HTTP_200_OK,
    summary="Atualização do produto", description=UpdateDescription.PRODUCT_UPDATE_DESCRIPTION,)
async def update_product(code: str, product: ProductUpdated):
    await product_rules.update_by_code(code, product)
 

@product_route.delete("/remove/code/{code}", status_code=status.HTTP_200_OK, summary="Remoção do Produto",
    description=DeleteDescription.PRODUCT_DELETE_DESCRIPTION,)
async def remove_product(code: str):
    await product_rules.remove_by_code(code)
 

@product_route.get("/code/{code}",status_code=status.HTTP_200_OK,
response_model=ProductGeneral,summary="Pesquisar pelo produto", description=CodeDescription.GET_PRODUCT_CODE_DESCRIPTION,)
async def get_product_by_code(code: str):
    product = await product_rules.search_by_code(code, True)
    return product
 

@product_route.get("/sku/{sku}", status_code=status.HTTP_200_OK,response_model=ProductGeneral,
summary="Pesquisar pelo produto", description=SkuDescription.GET_PRODUCT_SKU_DESCRIPTION,)
async def get_product_by_sku(sku: str):
    product = await product_rules.search_by_sku(sku, True)
    return product
 

@product_route.get("/name/{name}",status_code=status.HTTP_200_OK,response_model=List[ProductGeneral],
summary="Pesquisar pelo Produto", description=NameDescription.GET_PRODUCT_NAME_DESCRIPTION,)
async def get_product_by_code(name: str):
    product = await product_rules.search_by_name(name, True)
    return product
 

@product_route.get("/category/{category}",status_code=status.HTTP_201_CREATED,response_model=List[ProductGeneral],
summary="Pesquisar pela categoria", description=CategoryDescription.GET_PRODUCT_CATEGORY_DESCRIPTION,)
async def get_products_by_category(category: str):
    product = await product_rules.search_by_category(category, True)
    return product
 

@product_route.get("/",status_code=status.HTTP_200_OK,response_model=List[ProductGeneral],
    summary="Pesquisar todos os produtos", description=ProductDescription.GET_ALL_DESCRIPTION)
async def get_all_products() -> List[ProductGeneral]:
    all = await product_rules.search_all()
    return all
