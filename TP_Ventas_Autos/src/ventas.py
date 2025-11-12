from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from datetime import datetime
from src.database import get_session
from src.models import Venta, VentaCreate, Auto

router = APIRouter()

# =========================================================
# REGLA DE NEGOCIO: total = cantidad * precio
# =========================================================
def _validar_total_venta(session: Session, data: dict):
    auto = session.get(Auto, data["auto_id"])
    if not auto:
        raise HTTPException(status_code=400, detail="El auto_id no existe")

    total_esperado = round(auto.precio * data["cantidad"], 2)
    if round(data["total"], 2) != total_esperado:
        raise HTTPException(
            status_code=400,
            detail=f"Total inconsistente. Debería ser {total_esperado} (= precio*cantidad)"
        )

# =========================================================
# ENDPOINTS DE VENTAS
# =========================================================

@router.get("/", summary="Listar todas las ventas")
def listar_ventas(session: Session = Depends(get_session)):
    ventas = session.exec(select(Venta)).all()
    return ventas


@router.post("/", summary="Registrar una nueva venta")
def crear_venta(venta_data: VentaCreate, session: Session = Depends(get_session)):
    data = venta_data.dict()
    if isinstance(data["fecha"], str):
        data["fecha"] = datetime.strptime(data["fecha"], "%Y-%m-%d").date()

    _validar_total_venta(session, data)

    venta = Venta(**data)
    session.add(venta)
    session.commit()
    session.refresh(venta)
    return venta


@router.get("/{venta_id}", summary="Obtener venta por ID")
def obtener_venta(venta_id: int, session: Session = Depends(get_session)):
    venta = session.get(Venta, venta_id)
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta


@router.put("/{venta_id}", summary="Actualizar datos de una venta")
def actualizar_venta(venta_id: int, datos: VentaCreate, session: Session = Depends(get_session)):
    venta = session.get(Venta, venta_id)
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")

    data = datos.dict()
    if isinstance(data["fecha"], str):
        data["fecha"] = datetime.strptime(data["fecha"], "%Y-%m-%d").date()

    _validar_total_venta(session, data)

    for field, value in data.items():
        setattr(venta, field, value)

    session.add(venta)
    session.commit()
    session.refresh(venta)
    return venta


@router.delete("/{venta_id}", summary="Eliminar una venta")
def eliminar_venta(venta_id: int, session: Session = Depends(get_session)):
    venta = session.get(Venta, venta_id)
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    session.delete(venta)
    session.commit()
    return {"mensaje": f"Venta con ID {venta_id} eliminada correctamente"}