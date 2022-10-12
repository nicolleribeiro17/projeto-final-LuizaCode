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
     
        $ .\ambientevirtual\Scripts\activate     
        
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
 
 </details>
 
 
