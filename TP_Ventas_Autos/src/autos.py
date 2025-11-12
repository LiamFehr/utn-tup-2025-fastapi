from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional
from sqlmodel import Session, select, col
from src.database import get_session
from src.models import Auto, AutoCreate

router = APIRouter()

# =========================================================
# ENDPOINTS AUTOS
# =========================================================

@router.get("/", summary="Listar todos los autos")
def listar_autos(
    skip: int = 0,
    limit: int = Query(100, le=200),
    session: Session = Depends(get_session)
):
    autos = session.exec(select(Auto).offset(skip).limit(limit)).all()
    return autos


@router.get("/buscar", summary="Buscar autos por filtros")
def buscar_autos(
    marca: Optional[str] = None,
    modelo: Optional[str] = None,
    anio_min: Optional[int] = Query(None, ge=1900),
    anio_max: Optional[int] = Query(None, le=2030),
    precio_min: Optional[float] = Query(None, ge=0),
    precio_max: Optional[float] = Query(None, ge=0),
    session: Session = Depends(get_session),
):
    stmt = select(Auto)
    if marca:
        stmt = stmt.where(col(Auto.marca).ilike(f"%{marca}%"))
    if modelo:
        stmt = stmt.where(col(Auto.modelo).ilike(f"%{modelo}%"))
    if anio_min is not None:
        stmt = stmt.where(Auto.anio >= anio_min)
    if anio_max is not None:
        stmt = stmt.where(Auto.anio <= anio_max)
    if precio_min is not None:
        stmt = stmt.where(Auto.precio >= precio_min)
    if precio_max is not None:
        stmt = stmt.where(Auto.precio <= precio_max)

    autos = session.exec(stmt).all()
    return autos


@router.post("/", summary="Crear un auto nuevo")
def crear_auto(auto_data: AutoCreate, session: Session = Depends(get_session)):
    auto = Auto(
        marca=auto_data.marca,
        modelo=auto_data.modelo,
        anio=auto_data.anio,
        precio=auto_data.precio
    )
    session.add(auto)
    session.commit()
    session.refresh(auto)
    return auto


@router.get("/{auto_id}", summary="Obtener auto por ID")
def obtener_auto(auto_id: int, session: Session = Depends(get_session)):
    auto = session.get(Auto, auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return auto


@router.put("/{auto_id}", summary="Actualizar un auto existente")
def actualizar_auto(auto_id: int, datos: AutoCreate, session: Session = Depends(get_session)):
    auto = session.get(Auto, auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")

    auto.marca = datos.marca
    auto.modelo = datos.modelo
    auto.anio = datos.anio
    auto.precio = datos.precio

    session.add(auto)
    session.commit()
    session.refresh(auto)
    return auto


@router.delete("/{auto_id}", summary="Eliminar un auto")
def eliminar_auto(auto_id: int, session: Session = Depends(get_session)):
    auto = session.get(Auto, auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    session.delete(auto)
    session.commit()
    return {"mensaje": f"Auto con ID {auto_id} eliminado correctamente"}