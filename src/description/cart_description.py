class CreationDescription:
    CART_CREATION_DESCRIPTION = """
    Criar um carrinho de compras associado a um usuário e adicionar itens ao carrinho.
 
    Se o carrinho for criado corretamente a API retornará sucesso (código HTTP 201),
    e no corpo da resposta um registro com o campo `codigo`, que é o código do novo carrinho em nosso sistema.
        """
 
 
class UpdateDescription:
    CART_UPDATE_DESCRIPTION = """
    Atualização do carrinho.
   
    Se o carrinho for atualizado corretamente a API retornará OK (código HTTP 200).
    """
 
class DeleteDescription:
    CART_DELETE_DESCRIPTION = """
    Remoção de um carrinho:
   
    Se o carrinho for deletado corretamente a API retornará OK (código HTTP 200)
    """
