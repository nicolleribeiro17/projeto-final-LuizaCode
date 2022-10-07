from typing import List

from pydantic import BaseModel, Field

import service.product_rules as product_rules
from fastapi import APIRouter, status
from models.product import Product, ProductGeneral, ProductUpdated, ProductCode
# Minha rota API de Produtos
product_route = APIRouter(prefix="/api/products",tags=["Produtos"],)

product_CREATION_DESCRIPTION = """
Criação de um novo Produto. Para registrar uma nova Produto:

- `nome`: Deve ter nome único.
- `artista`: Deve ter uma pessoa artista.
- `tempo`: Opcionalmente pode ter um tempo. Se informado deve ser
maior que 0 (zero).

Se a Produto for criada corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`codigo`, que é o código da nova Produto em nosso sistema.
"""

# Colocamos este modelo aqui, SOMENTE para ficar perto da documentação.
# Seria apropriado criar um 'modelo' para cada erro??

class HasAnotherEmail(BaseModel):
    """
    Outro Produto possui o mesmo nome que a Produto corrente.
    """
    message: str = Field(..., description="Mensagem com a causa do problema")

    class Config:
        schema_extra = {
            "example": {
            "message": "Há outro Produto com este nome",
            }}


@product_route.post("/", summary="Criação de novo Produto",description=product_CREATION_DESCRIPTION,
    status_code=status.HTTP_201_CREATED, response_model = ProductCode,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Já temos outro Produto com este email.",
            "model": HasAnotherEmail
        }
    },
)

async def create_new_product(product: Product):
    new_product = await product_rules.insert_new_product(product)
    return new_product


@product_route.put("/{codigo}",status_code=status.HTTP_202_ACCEPTED,
    summary="Atualização do Produto",
    description="Atualiza um Produto pelo código",
)
async def update_product(code: str, product: ProductUpdated):
    await product_rules.update_by_code(code, product)


@product_route.delete("/{code}", status_code=status.HTTP_202_ACCEPTED, summary="Remoção do Produto",
    description="Remove o Produto pelo código",)

async def remove_product(code: str):
    # Remove uma Produto pelo código
    await product_rules.remove_by_code(code)


@product_route.get("/{code}",response_model=ProductGeneral,summary="Pesquisar pelo Produto",
    description="Pesquisar um Produto pelo código",)
async def get_product_by_code(code: str):
    # Pesquisa a Produto pelo código.
    product = await product_rules.search_by_code(code, True)
    return product


@product_route.get("/",response_model=List[ProductGeneral],
    summary="Pesquisar todos os Produtos",
    description="Pesquisar por todos os Produtos.",)

async def get_all_products() -> List[ProductGeneral]:
    # Pesquisar por todos as Produtos (sem um filtro)
    all = await product_rules.search_all()
    return all
