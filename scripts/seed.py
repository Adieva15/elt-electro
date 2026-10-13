from app.db import SessionLocal
from app.models import Product, Category

categories = [
    {"name": "Новости", "slug": "news"},
    {"name": "Обзоры", "slug": "reviews"},
]

items = [

    {
        "title": "Смартфон",
        "price": 29999,
        "is_sale": True,
        "category_slug": "news",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFV-H2ZVH987Wz3JkH12sCBEFIak8SCmjxCZaUlx7hvQ&s=10",
    },
    {
        "title": "Планшет",
        "price": 34999,
        "is_sale": False,
        "category_slug": "news",
        "image_url": "https://placehold.co/200x200?text=Планшет",
    },
    {
        "title": "Наушники TWS",
        "price": 7999,
        "is_sale": True,
        "category_slug": "news",
        "image_url": "https://placehold.co/200x200?text=Наушники",
    },
    {
        "title": "Умные часы",
        "price": 15999,
        "is_sale": False,
        "category_slug": "news",
        "image_url": "https://placehold.co/200x200?text=Часы",
    },
    {
        "title": "Роутер Wi-Fi 7",
        "price": 12999,
        "is_sale": False,
        "category_slug": "news",
        "image_url": "https://placehold.co/200x200?text=Роутер",
    },

    {
        "title": "Ноутбук",
        "price": 59999,
        "is_sale": False,
        "category_slug": "reviews",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnsG5LdCphn-qfjsKpJtCV1bDQJdig1vSxDq3hy0Yofg&s=10",
    },
    {
        "title": "Монитор",
        "price": 24999,
        "is_sale": False,
        "category_slug": "reviews",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgXOQLXSy0AkUUtSwuUK3OzKqFUoCbXyfkNYQUwgKevg&s=10",
    },
    {
        "title": "Клавиатура механическая",
        "price": 6999,
        "is_sale": False,
        "category_slug": "reviews",
        "image_url": "https://placehold.co/200x200?text=Клавиатура",
    },
    {
        "title": "Мышь беспроводная",
        "price": 2999,
        "is_sale": True,
        "category_slug": "reviews",
        "image_url": "https://placehold.co/200x200?text=Мышь",
    },
    {
        "title": "Аэрогриль",
        "price": 8999,
        "is_sale": False,
        "category_slug": "reviews",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRv8MG1Qc7-e1tpLr06-GlMUNmghGM3z6uhIZcVqBrSLQ&s=10",
    },
]

def run():
    db = SessionLocal()

    if db.query(Category).count() == 0:
        db.add_all([Category(**c) for c in categories])
        db.commit()
        print(f"Seeded {len(categories)} categories")
    else:
        print("Categories already exist, skipping")

    if db.query(Product).count() == 0:
        slug_to_id = {c.slug: c.id for c in db.query(Category).all()}
        for item in items:
            item = item.copy()
            slug = item.pop("category_slug")
           
            db.add(Product(category_id=slug_to_id.get(slug), **item))
        db.commit()
        print(f"Seeded {len(items)} products")
    else:
        print("Products already exist, skipping")

    db.close()

if __name__ == "__main__":
    run()