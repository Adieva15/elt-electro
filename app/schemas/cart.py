from pydantic import BaseModel, Field
from app.schemas.product import ProductRead

class CartItemAdd(BaseModel):
    product_id: int
    quantity: int=Field(default=1, ge=1)

class CartItemUpdate(BaseModel):
    quantity: int= Field(ge=1)

class CartItemRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    product: ProductRead

    model_config = {"from_attributes": True}

class CartRead(BaseModel):
    id: int
    session_id: str
    items: list[CartItemRead]

    model_config = {"from attributes": True}