"""
Todas as configurações do projeto estarão
centralizadas neste arquivo.
"""
from os import environ
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings

# Classe das configurações
class Configuracao(BaseSettings):
    # URI/String de conexão com o meu banco de dados.
    database_uri: str 

def iniciar_configuracao():
    # Carregando as variáveis de ambientes definidas
    # no arquivo .env (se ele existir)
    load_dotenv()
    return Configuracao()

# Como as configurações são de minha aplicação
# Vou instanciá-la apenas uma vez e 'globalmente'
configuracao = iniciar_configuracao()
