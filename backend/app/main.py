from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine, Session
from app.core.seed import seed_database
from app.models import flights
from app.routers import flights as flights_router
from app.routers import externalapi as stackoverflow_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    db = Session()
    try:
        #? Inicializacion del proyecto con seed de datos 
        seed_database(db)
    finally:
        db.close()

    yield


app = FastAPI(
    title="Vuelos & StackExchange API",
    description="API que centraliza datos de vuelos en Mexico y consultas de StackExchange",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flights_router.router)
app.include_router(stackoverflow_router.router)


@app.get("/", tags=["Health"], summary="Estado de la API")
def health_check():
    return {
        "status": "ok",
        "service": "vuelos-stack-api",
        "docs": "/docs"
    }