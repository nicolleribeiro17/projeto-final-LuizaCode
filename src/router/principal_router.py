from fastapi import APIRouter


principal_route = APIRouter(prefix="",tags=["Principal",],)


@principal_route.get("/", response_model=str, summary="Diga oi.",
    description="Rota principal em que se diz um '`Oi`'.",)
async def dizer_ola():
    return "Oi"
