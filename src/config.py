"""
Todas as configurações do projeto estarão
centralizadas neste arquivo.
"""
from os import environ
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings


class Configuracao(BaseSettings):
    database_uri: str 

def iniciar_configuracao():
    load_dotenv()
    return Configuracao()


configuracao = iniciar_configuracao()
