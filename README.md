![Projeto final Luiza Code](https://user-images.githubusercontent.com/112034898/195216177-e8dc059f-cbcf-41e0-8010-e834c06e1ea8.png)

Projeto de um carrinho de compras de uma papelaria utilizando FastAPI e MongoDB.

<h2 align="center"> FINALIDADE </h2>

Neste projeto iremos construir uma API em FastAPI para realizar a compra de itens de papelaria. 

O cadastro de clientes da nossa papelaria será realizado por meio dos seguintes dados: 
+ `Nome:` Consiste no nome completo do usuário. Esse campo é texto obrigatório que deve conter no mínimo 5 caracteres sem espaços e no máximo 128.
+ `Email: `Consiste no email do usuário. Esse campo é texto obrigatório que deverá ser unico.

O produto irá conter as seguintes informações: 
+ `Nome:` Consiste no nome do produto. 
+ `Descrição:` Consiste em uma descrição detalhada sobre o produto.
+ `Preço:` Consiste no valor do produto.
+ `Quantidade disponivel em estoque:`Consiste na quantidade de itens que temos em estoque para lhe atender. 
+ `Categoria:` Consite na condição em que o produto se encaixa - Exemplo: Escrita, Corte.

Já o nosso carrinho: 
+ `Usuário:` Consiste no usuário que realizou a compra. 
+ `Pedido:` Consiste na lista de itens comprados. 
+ `Total do pedido:`  Consiste no valor total de todos os itens comprados. 
+ `Total de itens:` Consiste na quantidade total de itens.



<h2 align="center"> ETAPAS DE DESENVOLVIMENTO </h2>

<details><summary><strong><h4>Etapa 00: Instalação, Clonando o Repositório, Criando o Ambiente Virtual e Instalando os Requerimentos.</strong></h4></summary>

  
  Antes de começar, você vai precisar instalar em sua máquina a seguinte ferramenta: [Python](https://python.org.br), além disto é importante que tenha ter um editor para trabalhar com o código, recomendamos o: [VSCode](https://code.visualstudio.com/).

  + Clonando o Repositório.
    
      No seu VSCode, será preciso dar o seguinte comando:
   
         $ git clone https://github.com/nicolleribeiro17/projeto-final-LuizaCode.git
  
  + Criando um ambiente virtual:
    
      Windows: 
       
         $ python -m venv venv 
         
      Linux: 
      
        $ python3.9 -m venv venv
        
  + Ativando o ambiente virtual:

     Windows:
     
        $ .\venv\Scripts\activate     
        
     Linux: 
     
        $ source venv/bin/activate
        
  + Instalando os Requerimentos: 

        $ pip install -r requirements.txt
        
  + Para executar o servidor da FastAPI, deve-se: 

     Acessar o diretório src, o qual contém os arquivos relacionados a aplicação: 
     
        $ cd src 
        
     Após acessar, dar o seguinte comando: 
     
        uvicorn --reload main:app
        
      Verificar se a aplicação foi de fato executada: 
      
        http://localhost:8000
        
      Caso for, será retornado um "Olá, bem vindos a papelaria do Luiza Code.  
 
 </details>
 
 <details><summary><h4>Etapa 01: Estruturas de Módulos.</h4></summary>


Organizamos a estrutura do nosso projeto em varias módulos, sendo que, cada uma realiza uma função dentro do projeto. Portanto, iremos ter as seguintes pastas: 

 - [`src`](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/tree/main/src): Pasta principal da aplicação.
   -  [`models`](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/tree/main/src/models): Modelagem de todo o código, o qual identifica os campos que o usuário, produto, carrinho e orer vai possuir.
   -  [`router`](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/tree/main/src/router): Módulos para de _controle_ e/ou _comunicação_ com o 
  FastAPI.
   -  [`service`](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/tree/main/src/service): Módulos para as regras (casos de uso) da 
  aplicação.
   - [`server`](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/tree/main/src/server): Módulo para persistência (repositório) 
  com o banco de dados.
   - [`descriptions`](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/tree/main/src/description): Local onde colocamos todas as descrições feitas pela requisição web.
   - [`main.py`](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/blob/main/src/main.py): Principal.
   - [`config.py`](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/blob/main/src/config.py): Configuração;
   
  
  
  + Como realizar:

  Foi criado pastas e arquivos de acordo considerando o que achamos necessário, seguindo a documentação. Nessa criação, as rotas da API Rest foram definidas com o [APIRouter](https://fastapi.tiangolo.com/tutorial/bigger-applications). 
  
   + Executando o servidor: 

          uvicorn --reload main:app
          
   + Acesso a aplicação: 
  
      Teste a aplicação acessando

          http://localhost:8000

      Ela irá lhe dizer um "Olá mundo, bem vindo a papelaria do Luiza Code"
    

    
   + Testando as APIs criadas
   
   
      O arquivo [testes.http](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/blob/main/testes.http) ou [Swagger](http://localhost:8000/docs/) será utilizado para realizar testes.
   
 
 </details>
 
 
 
<details><summary><h4>Etapa 02: Endpoints APIs. </h4></summary>

  <details><summary><h4>Usário. </h4></summary>

  + Retorna todos os usuários: 

      http
        GET /api/users



  + Cadastra um novo cliente:

      http
        POST /api/users


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `name`      | `string` | *Obrigatório*. O nome do cliente|
      | `email`      | `EmailStr` | *Obrigatório*. O email do cliente |
      | `password`      | `string` | *Obrigatório*. A senha do cliente |
      | `is_active`      | `bool` | *Obrigatório*. Usuário está ativo ou não|
      | `is_admin`      | `bool` | *Obrigatório*. Usuário é admin ou não |



  + Atualizar cliente por meio do seu código:

      http
        PUT api/users/update/{code}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `code`      | `string` | *Obrigatório*. O código do usuário que você quer atualizar. |
      | `name`      | `string` | *Opcional*. Nome do cliente|
      | `email`      | `EmailStr` | *Opcional*. Email do cliente |
      | `password`      | `string` | *Opcional*. Senha do cliente |
      | `is_active`      | `bool` | *Opcional*. Usuário está ativo ou não|
      | `is_admin`      | `bool` | *Opcional*. Usuário é admin ou não |




  + Deletar cliente

      http
        DELETE api/users/delete/{code}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `code`      | `string` | *Obrigatório*. O código do usuário que você quer deletar. |


  + Retorna um cliente pelo seu código:

      http
        GET api/users/code/{code}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `code`      | `string` | *Obrigatório*. Código do usuário. |



  + Retorna um cliente pelo seu email:

      http
        GET api/users/email/{email}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `email`      | `EmailStr` | *Obrigatório*. Email do usuário. |


</details>

  <details><summary><h4>Endereço. </h4></summary>

  + Cadastrar uma novo endereço para um usuário:

      http
        POST /api/address

      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `user_code`      | `string` | *Obrigatório*. Código cliente|
      | `email`      | `EmailStr` | *Obrigatório*. Email do cliente |
      | `number`      | `int` | *Obrigatório*. Número da residência|
      | `zip_code`      | `string` | *Obrigatório*. CEP|
      | `district`      | `string` | *Obrigatório*. Bairro|
      | `city`      | `string` | *Obrigatório*. Nome da cidade|
      | `state`      | `string` | *Obrigatório*. Sigla do estado|
      | `is_delivery`      | `bool` | *Obrigatório*. Se o produto foi entregue |


  + Retorna todos os endereços do usuário através do email:

      http
        GET /api/address/email/{email}

      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `email`      | `EmailStr` | *Obrigatório*. Email do usuário que você quer os endereços |
  
</details>

<details><summary><h4>Produto. </h4></summary>


  + Retorna todos os produtos:

      http
        GET /api/products


  

  + Cadastra um novo produto:

      http
        POST /api/products


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `name`      | `string` | *Obrigatório*. Nome do produto|
      | `description`      | `string` | *Obrigatório*. Descrição do produto |
      | `price`      | `float` | *Obrigatório*. Preço do produto |
      | `units_in_stock`      | `int` | *Obrigatório*. Unidades do produto em estoque|
      | `image`      | `string` | *Obrigatório*. Imagem produto |
      | `category`      | `string` | *Obrigatório*. Categoria do produto |
      | `sku`      | `string` | *Obrigatório*. SKU do produto |





  + Atualizar produto por meio de seu código:

      http
        PUT api/products/update/{code}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `code`      | `string` | *Obrigatório*. O código do produto que você quer atualizar. |
      | `name`      | `string` | *Opcional*. Nome do produto|
      | `description`      | `string` | *Opcional*. Descrição do produto |
      | `price`      | `float` | *Opcional*. Preço do produto |
      | `units_in_stock`      | `int` | *Opcional*. Unidades do produto em estoque|
      | `image`      | `string` | *Opcional*. Imagem produto |
      | `category`      | `string` | *Opcional*. Categoria do produto |
      | `sku`      | `string` | *Opcional*. SKU do produto |





  + Deleta produto por meio de seu código:

      http
        DELETE api/products/delete/{code}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `code`      | `string` | *Obrigatório*. O código do usuário que você quer deletar. |




  + Retorna um produto pelo seu código:

      http
        GET api/products/code/{code}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `code`      | `string` | *Obrigatório*. Código do produto. |





  + Retorna um produto pelo seu SKU:

      http
        GET api/products/sku/{sku}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `sku`      | `string` | *Obrigatório*. SKU do produto. |



  + Retorna os produtos pela categoria:

      http
        GET api/products/category/{category}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `category`      | `string` | *Obrigatório*. Categoria do produto. |



  

  + Retorna os produtos pelo nome:

      http
        GET api/products/name/{name}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `name`      | `string` | *Obrigatório*. Nome do produto. |


  
</details>


<details><summary><h4>Carrinho. </h4></summary>
   

  + Cadastro de um novo carrinho:

      http
        POST /api/cart


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `user_code`      | `string` | *Obrigatório*. Código do usuário|
      | `email`      | `EmailStr` | *Obrigatório*. Email do usuário |
      | `name`      | `string` | *Obrigatório*. Nome do produto|
      | `description`      | `string` | *Obrigatório*. Descrição do produto |
      | `price`      | `float` | *Obrigatório*. Preço do produto |
      | `units_in_stock`      | `int` | *Obrigatório*. Unidades do produto em estoque|
      | `image`      | `string` | *Obrigatório*. Imagem produto |
      | `category`      | `string` | *Obrigatório*. Categoria do produto |
      | `sku`      | `string` | *Obrigatório*. SKU do produto |
      | `quantity`      | `int` | *Obrigatório*. Quantidade do produto |



  + Atualizar a quantidade de um produto no carrinho por meio de seu código:

      http
        PUT api/cart/update/{code}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `code`      | `string` | *Obrigatório*. O código do produto que você quer atualizar. |
      | `quantity`      | `int` | *Obrigatório*. Quantidade do produto |

  + Deletar o produto no carrinho por meio de seu código:

      http
        PUT api/cart/update/{code}


      | Parâmetro   | Tipo       | Descrição                                   |
      | :---------- | :--------- | :------------------------------------------ |
      | `user_code`      | `string` | *Obrigatório*. Código do usuário|
      | `email`      | `EmailStr` | *Obrigatório*. Email do usuário |      
      | `code`      | `string` | *Obrigatório*. O código do produto que você quer atualizar. |
      | `quantity`      | `int` | *Obrigatório*. Quantidade do produto |


</details>


</details>



<details><summary><strong><h4>Etapa 03: Usuário.</strong></h4></summary>

  + Instruções da etapa: 
    
      Com o banco de dados no MongoDB, vamos realizar o cadastro de um usuário, isso implica em utilizarmos a API para "enviar" a requisição de salvar o novo usuário nosso banco de dados.

        POST http://localhost:8000/api/users
        
      Antes de salvar o novo usuário, precisamos validar as seguintes regras:
       <pre>
       ✔️ O cliente deve informar um email válido (ao menos 3 caracteres, conter um @).
       ✔️ O e-mail do cliente deve ser único, ou seja, não há dois clientes no sistema com o mesmo e-mail. 
       ✔️ Podemos ter dois clientes com o mesmo nome; mas, cada um com um e-mail diferente.
       ✔️ Ao pesquisarmos o email válido do cliente, será apresentado seus dados. 
       ✔️ Ao remover o usuário cadastrado, será apagado todas as informações do mesmo. 
       </pre>
      Na API, se conseguirmos cadastrar o usuário no banco de dados, iremos retornar o código HTTP 201 (Criado/Created), e no corpo de resposta iremos informar apenas o código do usuário:
      
        {
          "code": "uuid v4"
        }

      Se ao tentar cadastrar um novo usuário, e houver um usuário já cadastrado com o mesmo email, a API retornará o código HTTP 409 (Conflito/Conflict) informando a seguinte mensagem:

        {
          "mensagem": "Há outro usuário com este email"
        }
        

  + Cadastrando um usuário: 
    
      Considerando que todas as validações para cadastrar um novo usuário vão estar no [Regras](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/blob/main/src/service/user_rules.py). Para cadastrar um novo usuário, iremos utilizar a função `create_new_user` no arquivo [Server](https://github.com/nicolleribeiro17/projeto-final-LuizaCode/blob/main/src/server/user_server.py)
       


</details>



<details><summary><strong><h4>Etapa 04: Produto.</strong></h4></summary>

  + Cadastro de Produtos: 
    
      Vamos realizar o cadastro de um produto, isso implica em utilizarmos a API para "enviar" a requisição de salvar o novo usuário nosso banco de dados.

        POST http://localhost:8000/api/products
        
      Antes de cadastrar um novo produto, será validado as seguintes regras:
      
       <pre>
       ✔️ Processo em que registra-se um novo produto no sistema.
       ✔️ Cada produto precisa ter pelo menos um nome, uma descrição e um código único.
       ✔️ Um produto pode ter um preço de venda, que é um valor superior a R$ 0,01.
       ✔️ O código do produto informado no processo de cadastro deve ser único, logo não há dois produtos no sistema com o mesmo código.
       ✔️ Os nomes dos produtos são únicos.
       </pre>
       
      Na API, se conseguirmos cadastrar o produto no banco de dados, iremos retornar o código HTTP 201 (Criado/Created), e no corpo de resposta iremos informar apenas o código do produto:
      
        {
          "code": "uuid v4"
        }

      Se ao tentar cadastrar um novo produto, e houver item com o mesmo SKU, a API retornará o código HTTP 409 (Conflito/Conflict) informando a seguinte mensagem:

        {
          "mensagem": "Há outro produto com este sku"
        }
        
        
  + Atualização de Produtos: 
    
      Vamos realizar a atualização de um produto, isso implica em utilizarmos a API para "enviar" a requisição de atualizar o produto em nosso banco de dados.

        PUT http://localhost:8000/api/products/update/{code}
        
      Antes de atualizar um produto, será validado as seguintes regras:
      
      <pre>
       ✔️ O código do produto não pode ser alterado.
       ✔️ O nome do produto pode ser alterado.
      </pre>        
        
  + Pesquisa de Produtos: 
  
      Vamos realizar a pesquisa de um produto, para realizar esse processo, temos três formas de executa-lo:
      
      Pesquisa um produto pelo nome:

        GET http://localhost:8000/api/products/name/
        
      Pesquisa um produto pelo categoria:   
        
        GET http://localhost:8000/api/products/category/
       
      Pesquisa um produto pelo SKU: 
      
        GET http://localhost:8000/api/products/sku/

  Logo, ao informar o nome, código ou SKU, será devolvido o produto desejado e suas informações.
  
  + Remoção de Produtos: 
  
     Etapa de remoção do produto: 
    
        DELETE  http://localhost:8000/api/products/remove/{code}
        

</details>

<details><summary><strong><h4>Etapa 05: Carrinho de Compras.</strong></h4></summary>

  O nosso carrinho de compras consiste em duas estapas: o carrinho aberto e o carrinho fechado. 
  
  
  + Carrinho em aberto: Você adiciona, atualiza ou remove os itens desejados para a compra. 
  
    O carrinho aberto, possui as seguintes funcionalidades e regras: 
    
        ✔️ Todo carrinho de compras deve conter um cliente e será validado se o mesmo existe.
        ✔️ Se há um produto um ou mais, deverá ser informado a quantidade de cada produto.
        ✔️ Verificar se o cliente já possui um carrinho aberto. Caso contrário criar um carrinho novo.
        ✔️ Ao adicionar um item no carrinho, o mesmo terá o valor total e quantidade de itens atualizado.
        ✔️ No carrinho novo, com base no produto informado, a quantidade é modificada.
        ✔️ Validar se produto existe no carrinho.
        ✔️ Atualizar o valor total e quantidade de itens do carrinho.
        ✔️ Se o carrinho zerar o número de itens, ou seja, o cliente removeu todos os itens do carrinho, o mesmo pode ser excluído.
        ✔️ Se o cliente e retornar os dados do carrinho e produtos.
        

  + Carrinho fechado: Passa por todo o processo do em aberto, mas resulta em pedido. 
  
      Já o carrinho fechado possoui as seguintes funcionalidades:
      
        ✔️ O cliente pode mudar o tipo do carrinho de compras para “fechado”.
        
  + Excluir o carrinho aberto e/ou fechado. 
  
        ✔️ Quer o carrinho seja aberto ou fechado, podemos remover o carrinho do sistema.

</details>

<h2 align="center"> CRIADORAS </h2>

<a href="https://www.linkedin.com/in/isadora-eduarda-6b2001180/" target="_blank_"><img height="15cm" src="https://img.shields.io/badge/ISADORA-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/> 
<a href="https://www.linkedin.com/in/juliana-abumansur-3359ba114/" target="_blank_"><img height="15cm" src="https://img.shields.io/badge/JULIANA-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/> 
<a href="https://www.linkedin.com/in/nicolle-ribeiro-89ab8b1b3/" target="_blank_"><img height="15cm" src="https://img.shields.io/badge/NICOLLE-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>

<a href="https://github.com/isadoraeduarda/" target="_blank_"><img height="15cm" src="https://img.shields.io/badge/ISADORA-100000?style=for-the-badge&logo=github&logoColor=white"/>
<a href="https://github.com/jtabumansur" target="_blank_"><img height="15cm" src="https://img.shields.io/badge/JULIANA-100000?style=for-the-badge&logo=github&logoColor=white"/>
<a href="https://github.com/nicolleribeiro17" target="_blank_"><img height="15cm" src="https://img.shields.io/badge/NICOLLE-100000?style=for-the-badge&logo=github&logoColor=white"/>

<h2 align="center"> STACK UTILIZADA </h2>

[![My Skills](https://skills.thijs.gg/icons?i=python,fastapi,vscode,github,scrum&theme=light)](https://skills.thijs.gg)
  

 
