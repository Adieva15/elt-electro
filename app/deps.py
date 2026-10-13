from collections.abc import Generator
from sqlalchemy.orm import Session
from fastapi import Cookie, Depends
import uuid

from app.db import SessionLocal
from app.models import Cart


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_or_create_cart(
        session_id: str | None = Cookie(default=None),
        db: Session = Depends(get_db),
):
    if not session_id:
        session_id = uuid.uuid4().hex
    cart = db.query(Cart).filter(Cart.session_id == session_id).first()
    if not cart:
        cart = Cart(session_id=session_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    return cart, session_id
# Cookie возвращается тоже, чтобы роутер мог её установить, если её не было.