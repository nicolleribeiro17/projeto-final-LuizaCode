from pydantic import BaseModel, Field
 
class HasAnotherEmail(BaseModel):
    """
    Outro usuário possui o mesmo email que o usuário corrente.
    """
    message: str = Field(..., description="Há outro usuário com este email")
 
 
class HasAnotherSku(BaseModel):
    """
    Outro produto possui o mesmo sku que o produto atual.
    """
    message: str = Field(..., description="Há outro produto com este sku")
 