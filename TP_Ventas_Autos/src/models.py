from typing import Optional, List
from datetime import date
from sqlmodel import SQLModel, Field, Relationship

# =========================================================
# MODELOS DE BASE DE DATOS
# =========================================================

class Auto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    marca: str
    modelo: str
    anio: int
    precio: float

    ventas: List["Venta"] = Relationship(back_populates="auto")


class Venta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: date
    cantidad: int
    total: float
    auto_id: int = Field(foreign_key="auto.id")

    auto: Optional[Auto] = Relationship(back_populates="ventas")


# =========================================================
# SCHEMAS DE VALIDACIÓN (ENTRADAS)
# =========================================================

class AutoCreate(SQLModel):
    marca: str = Field(min_length=1, max_length=50)
    modelo: str = Field(min_length=1, max_length=50)
    anio: int = Field(gt=1900, le=2030)
    precio: float = Field(gt=0)


class VentaCreate(SQLModel):
    fecha: date
    cantidad: int = Field(gt=0)
    total: float = Field(gt=0)
    auto_id: int