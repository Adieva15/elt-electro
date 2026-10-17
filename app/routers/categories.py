from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.config import settings
from app.deps import get_db
from app.models import Category
from app.routers.products import require_admin
from app.schemas.category import CategoryCreate, CategoryRead


router = APIRouter(prefix="/api/categories", tags=["categories"])

@router.get("", response_model=list[CategoryRead])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).order_by(Category.id).all()

@router.post("", response_model=CategoryRead, status_code=201, dependencies=[Depends(require_admin)])
def create_category(payload:CategoryCreate, db:Session=Depends(get_db)):
    if db.query(Category).filter(Category.slug == payload.slug).first():
        raise HTTPException(status_cose=409, detail="Skug already exists")
    category = Category(**payload.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category
