from typing import Optional
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(max_length=100)
    description: str
    price: float
    image: str
    code: int 
    sku: int

class ProductUpdated(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    image: Optional[str]
    code: int
    

class ProductCode(BaseModel):
    code: str = Field(..., description="Código do Produto, no formato uuid v4",)
     
    class Config:
        schema_extra = {
            "example": {
                "codigo": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6",
            }
        }    
class ProductGeneral(ProductCode, Product):
    ...
class SearchProducts(Product):
    _id: str
    code: str
    
    class Config:
        orm_mode = True

