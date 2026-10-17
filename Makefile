up:
    docker compose up --build -d

down:
    docker compose down

logs:
    docker compose logs -f app

test:
    docker compose run --rm app pytest -q

migrate: 
    docker compose run --rm app alembic revision --autogenerate -m "$(m)"

upgrade:
    docker compose run --rm app alembic upgrade head

seed:
    docker compose run --rm app python -m scripts.seed