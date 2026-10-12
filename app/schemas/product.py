from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    price: float = Field(gt=0)
    image_url: str | None = None
    is_sale: bool = False

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    title: str | None = None
    price: float | None = Field(default=None, gt=0)
    image_url: str | None = None
    is_sale: bool | None = None

class ProductRead(ProductBase):
    id: int

    model_config = {"from_attributes": True}