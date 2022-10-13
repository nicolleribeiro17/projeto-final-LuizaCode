 
class CreationDescription:
    USER_CREATION_DESCRIPTION = """
    Criação de um novo usuário:
   
    - `nome` Deve ter no minimo 6 caracteres.
    - `email`: Deve ter nome único.
    - `password`: Deve ter uma senha.
    - `is_active`: boolean.
    - `is_admin`: boolean.
   
   
    Se o usuário for criado corretamente a API retornará sucesso
    (código HTTP 201) e no corpo da resposta um registro com o campo
    `codigo`, que é o código do novo usuário em nosso sistema.
    """
 
 
class EmailDescription:
    GET_USER_EMAIL_DESCRIPTION = """
    Busca um usuário pelo seu email.
   
    Se o email do usuário for válido  API irá retornar OK (código HTTP 200),
    e no corpo da resposta um registro com os dados do usuário.
    """
 
class CodeDescription:
    GET_USER_CODE_DESCRIPTION = """
    Busca um usuário pelo seu código.
   
    Se o código do usuário for válido API irá retornar OK (código HTTP 200),
    e no corpo da resposta um registro com os dados do usuário.
    """
 
class UserDescription:
    GET_ALL_DESCRIPTION = """
    Busca todos os usuários cadastrados.
   
    Se o caminho estiver correto API irá retornar OK (código HTTP 200),
    e no corpo da resposta um registro com os dados dos usuários.
    """
 
 
class UpdateDescription:
    USER_UPDATE_DESCRIPTION = """
    Atualização de um usuário:
   
    Se o usuário for atualizado corretamente a API retornará OK (código HTTP 200).
 
"Atualizar quantidade do produto",
    description="Atualiza um usuário pelo código",
)
 
    """
 
 
class DeleteDescription:
    USER_DELETE_DESCRIPTION = """
    Remoção de um usuário:
   
    Se o usuário for deletado corretamente a API retornará OK (código HTTP 200)
    """
