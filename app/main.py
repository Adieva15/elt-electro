from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import health, products, categories


app = FastAPI(title="ELT-Electro")

app.include_router(health.router)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

app.include_router(products.router)
app.include_router(categories.router)

