from datetime import datetime
from fastapi import APIRouter, Depends
from models import User, UserResponse
from auth import get_current_active_user
from typing import Dict, Any

router = APIRouter(prefix="/protected", tags=["Protected Endpoints"])

@router.get("/test", response_model=Dict[str, Any])
async def protected_test_endpoint(current_user: User = Depends(get_current_active_user)):
    """
    Test endpoint that requires JWT authentication.
    Returns information about the authenticated user and server time.
    """
    return {
        "message": "¡Acceso autorizado! Este es un endpoint protegido.",
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email,
            "is_active": current_user.is_active,
            "created_at": current_user.created_at
        },
        "server_time": datetime.utcnow(),
        "endpoint": "protected_test"
    }

@router.get("/user-profile", response_model=UserResponse)
async def get_user_profile(current_user: User = Depends(get_current_active_user)):
    """
    Protected endpoint that returns the current user's profile information.
    Requires valid JWT token in Authorization header.
    """
    return current_user

@router.get("/dashboard")
async def user_dashboard(current_user: User = Depends(get_current_active_user)):
    """
    Protected dashboard endpoint that shows user-specific information.
    """
    return {
        "welcome_message": f"¡Bienvenido al dashboard, {current_user.username}!",
        "user_id": current_user.id,
        "account_status": "active" if current_user.is_active else "inactive",
        "member_since": current_user.created_at.strftime("%Y-%m-%d"),
        "last_accessed": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "features": [
            "Acceso a API completa",
            "Dashboard personalizado", 
            "Gestión de perfil",
            "Historial de actividad"
        ]
    }
