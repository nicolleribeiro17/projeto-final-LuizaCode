import asyncio

from motor.motor_asyncio import (AsyncIOMotorClient, AsyncIOMotorCollection,
                                 AsyncIOMotorDatabase)
from config import configuracao

def iniciar_cliente_mongo() -> AsyncIOMotorClient:
    cliente_mongo = AsyncIOMotorClient(configuracao.database_uri)
    cliente_mongo.get_io_loop = asyncio.get_event_loop
    return cliente_mongo


cliente_mongo = iniciar_cliente_mongo()

def obter_base_dados() -> AsyncIOMotorDatabase:
    return cliente_mongo.get_default_database()


def get_collection(nome_colecao: str) -> AsyncIOMotorCollection:
    bd = obter_base_dados()
    colecao = bd[nome_colecao]

    return colecao
