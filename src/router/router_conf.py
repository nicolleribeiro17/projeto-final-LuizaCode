from typing import Callable, Tuple

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from service.rules_exception import ExceptionNotFound, OtherExceptionRules, RulesException, OtherCodesExceptions
from router.user_router import user_route
from router.principal_router import principal_route
from router.product_router import product_route
from router.address_router import address_route
from router.cart_router import cart_route
from router.order_router import order_route

def ExceptionNotFound_Response(requisicao: Request, excecao: ExceptionNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "mensagem": excecao.mensagem
        }
    )


def OtherExceptionRules_Response(requisicao: Request, excecao: OtherExceptionRules):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "mensagem": excecao.mensagem
        }
    )


def Exception_Interceptor_Config(app: FastAPI) -> Tuple[Callable]:
    @app.exception_handler(ExceptionNotFound)
    async def Exception_Not_Found_Interceptor(request: Request, exc: ExceptionNotFound):
        return ExceptionNotFound_Response(request, exc)

    @app.exception_handler(OtherExceptionRules)
    async def Other_Exception_Rules_Interceptor(request: Request, exc: OtherExceptionRules):
        return OtherExceptionRules_Response(request, exc)

    return (
        Exception_Not_Found_Interceptor,
        Other_Exception_Rules_Interceptor,
    )


def configurar_rotas(app: FastAPI):
    app.include_router(principal_route)
    app.include_router(user_route)
    app.include_router(address_route)
    app.include_router(product_route)    
    app.include_router(cart_route)
    app.include_router(order_route)


##CONFIGURACAO DE CORS, NAO SERA NECESSARIO PARA O NOSSO PROJETO

# def configurar_api_rest(app: FastAPI):
#     # Configurando o CORS
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=["*"],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
#     # Configurando os interceptadores
#     Exception_Interceptor_Config(app)


def criar_aplicacao_fastapi():
    app = FastAPI()
    configurar_rotas(app)

    return app
