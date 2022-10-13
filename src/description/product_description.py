class CreationDescription:
    PRODUCT_CREATION_DESCRIPTION = """
    Criação de um novo produto.
 
    - `name`: Nome do produto.
    - `description`: Descrição do produto.
    - `price`: Preco do produto - deve ser maior do que R$ - 0.01.
    - `image`: Imagem do produto.
    - `units_in_stock`: Quantidadade em estoque do produto. Deve ser superior a 0.
    - `category`: Categoria do produto.
    - `sku`: Maneira de identificar um produto no estoque.
 
 
    Se o produto for criado corretamente a API retornará sucesso
    (código HTTP 201) e no corpo da resposta um registro com o campo
    `codigo`, que é o código da nova Produto em nosso sistema.
    """
 
class SkuDescription:
    GET_PRODUCT_SKU_DESCRIPTION = """
    Busca um produto pelo seu sku.
 
    Se o SKU do produto for válido  API irá retornar OK (código HTTP 200),
    e no corpo da resposta um registro com os dados do produto.
    """
 
class CodeDescription:
    GET_PRODUCT_CODE_DESCRIPTION = """
    Busca um produto pelo seu código.
 
    Se o código do produto for válido API irá retornar OK (código HTTP 200),
    e no corpo da resposta um registro com os dados do produto.
    """
 
class NameDescription:
    GET_PRODUCT_NAME_DESCRIPTION = """
    Busca produto pelo seu nome. Os produtos podem ter nomes iguais.
 
    Se a solicitação for válida, a API irá retornar OK (código HTTP 200),
    e no corpo da resposta um registro com os dados do produto.
    """
 
class CategoryDescription:
    GET_PRODUCT_CATEGORY_DESCRIPTION = """
    Busca produtos pelo sua categoria.  
 
    Se a solicitação for válida, a API irá retornar OK (código HTTP 200),
    e no corpo da resposta um registro com os dados do produto. ?
    """
 
class ProductDescription:
    GET_ALL_DESCRIPTION = """
    Busca todos os produtos cadastrados.
 
    Se a solicitação for válida, a API irá retornar OK (código HTTP 200),
    e no corpo da resposta um registro com os dados dos produtos.
    """
 
class UpdateDescription:
    PRODUCT_UPDATE_DESCRIPTION = """
    Atualização de um produto pelo seu código:
   
    Se o produto for atualizado corretamente a API retornará OK (código HTTP 200).
    """
 
class DeleteDescription:
    PRODUCT_DELETE_DESCRIPTION = """
    Remoção de um produto pelo seu código:
   
    Se o produto for deletado corretamente a API retornará OK (código HTTP 200)
    """
 
