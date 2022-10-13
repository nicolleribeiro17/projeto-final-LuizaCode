from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(...,max_length=100)
    description: str = Field(...,max_length=100)
    price: float = Field(...,ge=0.01)
    units_in_stock: int = Field(...,ge=0)
    image: str = Field(...,max_length=100)
    category: str = Field(...,max_length=100)
    sku: str = Field(...,min_length=3, unique=True)

class ProductUpdated(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    units_in_stock:Optional[int]
    image: Optional[str]
    category: Optional[str]
    sku: Optional[str]

class ProductCode(BaseModel):
    code: str = Field(..., description="Codigo do Produto, no formato uuid v4")


class ProductGeneral(ProductCode, Product):
    ...

class SearchProducts(Product):
    code: str
    sku: str

   