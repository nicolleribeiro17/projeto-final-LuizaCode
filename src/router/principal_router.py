from fastapi import APIRouter

# Minha API da rota principal
rota_principal = APIRouter(prefix="",tags=["Principal",],)


@rota_principal.get("/", response_model=str, summary="Diga oi.",
    description="Rota principal em que se diz um '`Oi`'.",)
async def dizer_ola():
    return "Oi"
