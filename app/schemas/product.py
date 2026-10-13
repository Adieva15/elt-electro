from pydantic import BaseModel, Field

from app.schemas.category import CategoryRead

class ProductBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    price: float = Field(gt=0)
    image_url: str | None = None
    is_sale: bool = False
    category_id: int | None = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    title: str | None = None
    price: float | None = Field(default=None, gt=0)
    image_url: str | None = None
    is_sale: bool | None = None
    category_id: int | None = None

class ProductRead(ProductBase):
    id: int
    category: CategoryRead | None = None
    model_config = {"from_attributes": True}