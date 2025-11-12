import os
from sqlmodel import SQLModel, create_engine, Session

# =========================================================
# CONEXIÓN A POSTGRESQL
# =========================================================

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:liam@localhost:5432/autosdb"  # 👈 poné tu contraseña real acá
)

# echo=True muestra las consultas SQL en consola (útil para debug)
engine = create_engine(DATABASE_URL, echo=True)

# ---------- FUNCIÓN PARA CREAR LAS TABLAS ----------
def init_db():
    SQLModel.metadata.create_all(engine)

# ---------- SESIÓN DE BASE DE DATOS ----------
def get_session():
    with Session(engine) as session:
        yield session