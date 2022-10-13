class CreationDescription:
    ADDRESS_CREATION_DESCRIPTION = """
    Criação de um novo endereço para o usuario:
 
    - `street` Rua
    - `number` Numero
    - `zip_code`: CEP.
    - `district`: Bairro.
    - `city`: Cidade.
    - `state`: Estado (Apenas a sigla).
    - `is_delivery`: E endereco padrao para entrega.
 
 
    Se o endereço for criado corretamente a API retornará sucesso (código HTTP 201),
     e no corpo da resposta um registro com o campo `codigo`, que é o código do novo endereço em nosso sistema.
    """
 
 
 
class EmailDescription:
    GET_USER_EMAIL_DESCRIPTION = """
    Busca os endereços cadastrados de um usuário pelo seu email.
   
    Se o email do usuário for válido  API irá retornar OK (código HTTP 200),
    e no corpo da resposta um registro com os dados do usuário.
    """
 
 
 
 
