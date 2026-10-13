Health
GET  /health              — проверка, что сервер жив (для Docker healthcheck)

Товары
GET  /api/products                    — список товаров
GET  /api/products?category=news      — фильтр по категории (slug)
GET  /api/products?search=смартфон    — поиск по названию
GET  /api/products/{id}               — один товар по id
POST /api/products                    — создать товар (только админ)
PUT  /api/products/{id}               — изменить товар (только админ)
DELETE /api/products/{id}             — удалить товар (только админ)

Категории
GET  /api/categories      — список категорий (для табов)

Корзина
GET    /api/cart              — содержимое корзины (по session_id из cookie)
POST   /api/cart/items        — добавить товар {product_id, quantity}
PUT    /api/cart/items/{id}   — изменить количество
DELETE /api/cart/items/{id}   — удалить позицию


docker ps
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows

docker compose up -d db

docker compose ps

<!-- Если БД уже была создана ранее и данные не удалялись — миграции уже применены, но команда безопасна: -->
alembic upgrade head