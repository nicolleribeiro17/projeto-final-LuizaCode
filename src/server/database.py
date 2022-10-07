import asyncio

from motor.motor_asyncio import (AsyncIOMotorClient, AsyncIOMotorCollection,
                                 AsyncIOMotorDatabase)
from config import configuracao

# ---------------------------------------------------
# Cliente Mongo 'global'
# ---------------------------------------------------


def iniciar_cliente_mongo() -> AsyncIOMotorClient:
    print("URL***",configuracao.database_uri)
    cliente_mongo = AsyncIOMotorClient(configuracao.database_uri)
    cliente_mongo.get_io_loop = asyncio.get_event_loop
    return cliente_mongo


cliente_mongo = iniciar_cliente_mongo()

# ---------------------------------------------------
# Funções auxiliares para quem for trabalhar com
# a persistência.
# ---------------------------------------------------


def obter_base_dados() -> AsyncIOMotorDatabase:
    # Obtém a base de dados (database) padrão
    # (a que está na string de conexão)
    return cliente_mongo.get_default_database()


def get_collection(nome_colecao: str) -> AsyncIOMotorCollection:
    # Obtém a coleção informada da base de dados padrão.
    bd = obter_base_dados()
    colecao = bd[nome_colecao]

    return colecao
