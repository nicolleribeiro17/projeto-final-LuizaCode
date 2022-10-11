from typing import List
from pydantic import BaseModel, Field
from fastapi import APIRouter, status

import service.product_rules as product_rules
from models.product import Product, ProductGeneral, ProductUpdated, ProductCode

# Minha rota API de Produtos
product_route = APIRouter(prefix="/api/products",tags=["Products"],)

PRODUCT_CREATION_DESCRIPTION = """
Criação de um novo produto.

- `name`: Nome do produto .
- `description`: Descrição do produto.
- `price`: Preco do produto - deve ser maior do que R$ - 0.01
- `image`: Imagem do produto
- `units_in_stock`: Quantida em estoque do produto. Deve ser superior a 0.
- `category`: Imagem do produto
- `sku`: Maneira de identificar um produto no estoque 


Se a Produto for criada corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`codigo`, que é o código da nova Produto em nosso sistema.
"""

# Colocamos este modelo aqui, SOMENTE para ficar perto da documentação.
# Seria apropriado criar um 'modelo' para cada erro??

class HasAnotherSku(BaseModel):
    """
    Outro produto possui o mesmo sku que o produto atual.
    """
    message: str = Field(..., description="Mensagem com a causa do problema")

    class Config:
        schema_extra = {
            "example": {
            "message": "Há outro produto com este sku",
            }}


# POST - OK MAS NÃO APARECE COMO O USUARIO???
@product_route.post("/", summary="Criação de novo Produto",description=PRODUCT_CREATION_DESCRIPTION,
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
    new_product = await product_rules.insert_new_product(product)
    return new_product

# PUT 
@product_route.put("/update/code/{code}",status_code=status.HTTP_202_ACCEPTED,
    summary="Atualização do produto",
    description="Atualiza um produto pelo código",
)
async def update_product(code: str, product: ProductUpdated):
    await product_rules.update_by_code(code, product)

# DELETE 
@product_route.delete("/remove/code/{code}", status_code=status.HTTP_202_ACCEPTED, summary="Remoção do Produto",
    description="Remove o Produto pelo código",)

async def remove_product(code: str):
    # Remove uma Produto pelo código
    await product_rules.remove_by_code(code)

# GET CODE
@product_route.get("/code/{code}",response_model=ProductGeneral,summary="Pesquisar pelo produto",
    description="Pesquisar um produto pelo código",)
async def get_product_by_code(code: str):
    # Pesquisa a Produto pelo código.
    product = await product_rules.search_by_code(code, True)
    return product

# GET SKU
@product_route.get("/sku/{sku}",response_model=ProductGeneral,summary="Pesquisar pelo produto",
    description="Pesquisar um produto pelo sku",)
async def get_product_by_sku(sku: str):
    # Pesquisa a Produto pelo código.
    product = await product_rules.search_by_sku(sku, True)
    return product

# GET NAME 
@product_route.get("/name/{name}",response_model=List[ProductGeneral],summary="Pesquisar pelo Produto",
    description="Pesquisar um produto pelo nome",)
async def get_product_by_code(name: str):
    product = await product_rules.search_by_name(name, True)
    return product

# GET CATEGORIA
@product_route.get("/category/{category}",response_model=List[ProductGeneral],summary="Pesquisar pela categoria",
    description="Pesquisar uma categoria",)
async def get_products_by_category(category: str):
    product = await product_rules.search_by_category(category, True)
    return product

# GET ALL
@product_route.get("/",response_model=List[ProductGeneral],
    summary="Pesquisar todos os produtos",
    description="Pesquisar por todos os produtos.")

async def get_all_products() -> List[ProductGeneral]:
    # Pesquisar por todos as Produtos (sem um filtro)
    all = await product_rules.search_all()
    return all


