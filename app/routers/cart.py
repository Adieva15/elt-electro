from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.deps import get_db, get_or_create_cart
from app.models import CartItem, Product
from app.schemas.cart import CartRead, CartItemAdd, CartItemUpdate, CartItemRead


router = APIRouter(prefix="/api/cart", tags=["cart"])

@router.get("", response_model=CartRead)
def read_cart(cart_data=Depends(get_or_create_cart), response:Response=None):
    cart, session_id = cart_data
    response.set_cookie("session_id", session_id, httponly=True, samesite="lax")
    return cart

@router.post("/items", response_model=CartItemRead, status_code=201)
def add_item(
    payload: CartItemAdd,
    response: Response,
    cart_data = Depends(get_or_create_cart),
    db: Session=Depends(get_db),
):
    cart, session_id = cart_data
    response.set_cookie("session_id", session_id, httponly=True, samesite="lax")

    if not db.get(Product, payload.product_id):
        raise HTTPException(status_code=404, detail="Product not found")

    existing = (
        db.query(CartItem)
        .filter(CartItem.cart_id == cart.id, CartItem.product_id == payload.product_id)
        .first()
    )
    if existing:
        existing.quantity += payload.quantity
        db.commit()
        db.refresh(existing)
        return existing

    item = CartItem(cart_id=cart.id, product_id=payload.product_id, quantity=payload.quantity)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/items/{item_id}", response_model=CartItemRead)
def update_item(
    item_id: int,
    payload: CartItemUpdate,
    cart_data=Depends(get_or_create_cart),
    db: Session = Depends(get_db),
):
    cart, _ = cart_data
    item = db.get(CartItem, item_id)
    if not item or item.cart_id != cart.id:
        raise HTTPException(status_code=404, detail="Item not found")
    item.quantity = payload.quantity
    db.commit()
    db.refresh(item)
    return item

@router.delete("/items/{item_id}", status_code=204)
def delete_item(
    item_id: int,
    cart_data=Depends(get_or_create_cart),
    db: Session = Depends(get_db),
):
    cart, _ = cart_data
    item = db.get(CartItem, item_id)
    if not item or item.cart_id != cart.id:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()