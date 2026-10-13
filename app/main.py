from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, products, categories, cart
from app.routers import health, products, categories

from fastapi.responses import FileResponse


app = FastAPI(title="ELT-Electro")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,     # важно для cookie session_id
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(cart.router)

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.get("/", include_in_schema=False)
def index():
    return FileResponse("frontend/templates/market.html")