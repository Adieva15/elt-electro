from app.db import SessionLocal
from app.models import Product

items = [
    {"title": "Смартфон", "price": 29999, "is_sale": True,
     "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:...1"},
    {"title": "Ноутбук", "price": 59999, "is_sale": False,
     "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:...2"},
    
]

def run():
    db = SessionLocal()
    if db.query(Product).count() == 0:
        db.add_all([Product(**i) for i in items])
        db.commit()
    db.close()

if __name__ == "__main__":
    run()