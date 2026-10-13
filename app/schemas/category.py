from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    slug: str = Field(min_length=1, max_length=100)

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id:int

    model_config = {"form_attributes":True}