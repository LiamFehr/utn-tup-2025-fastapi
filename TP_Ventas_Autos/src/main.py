from fastapi import FastAPI
from src.database import init_db
from src.autos import router as autos_router
from src.ventas import router as ventas_router

app = FastAPI(
    title="API de Ventas de Autos - UTN",
    version="2.0.0",
    description="""
    Trabajo Práctico Final de la materia Programación Avanzada.  
    Implementación completa de un backend REST con FastAPI, SQLModel y PostgreSQL.
    """
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(autos_router, prefix="/autos", tags=["Autos"])
app.include_router(ventas_router, prefix="/ventas", tags=["Ventas"])