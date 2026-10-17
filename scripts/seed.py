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
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2fWCcN63PswRa5fyFeBy2-bih1fKR3Fn2GHgBgM3yv4ZkeF3Tp3RAPdc3UISxxFYgiFx9wppdp4GD2pFGlUqbxz34vvfk1deio6d4leE",
    },
    {
        "title": "Наушники TWS",
        "price": 7999,
        "is_sale": True,
        "category_slug": "news",
        "image_url": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcTn3R8zhLmUMOMKrpgSRnSugKydgGu3TawlAxR7ItoMe8cw8y9vbHrrcVX8tlaRt5WdgxppkbmpMvgVtDk7E3oXdAgBSWVkwCDadYmM5A-GXY5lAdPf_SBz",
    },
    {
        "title": "Умные часы",
        "price": 15999,
        "is_sale": False,
        "category_slug": "news",
        "image_url": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcS9DG7XyZwcfWO3zJ23Cju8k885gHWGjeDYgkhI0BgkeqxZr6Q_CzbKes6MI-BaVqyBByvzr5tNhdd7CJo00FkKaOEabB6-8y-RZyYhTPq1qibUO5cQe2XQiw",
    },
    {
        "title": "Роутер Wi-Fi 7",
        "price": 12999,
        "is_sale": False,
        "category_slug": "news",
        "image_url": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTNKLxU4kQCBR1QWRWKa7p7Z-mJTx16iFwZfs-prxsGWWFNYuKKmJv0Q2E6P5nWtmsMyn55h1SnTDYTyq0SpPuOzNpCiQdywfrB3hmALN4",
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
        "image_url": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcTUsFeVXvYv3C0ddby7yWGYn2QEt8BIviFq0AQdBEdXFG8FWcdZFxvlx3riCg0nGGAy4cOvgSXunAnFjsnBKyPU3BkA2EIKkp-k-LiyASDkkJRXFCTdLhVuAg",
    },
    {
        "title": "Мышь беспроводная",
        "price": 2999,
        "is_sale": True,
        "category_slug": "reviews",
        "image_url": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcRoYqb8TUZK_aMyVFhBEpJVD9PKNr9wzbPgayBu1LiiNBfb1-uJEt_LhrnZhbDeVCJd9rHMfY2a9kx68G-CGvCtW13XSiWQGVYHMerqDsqEbr2KOkCXAITG",
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