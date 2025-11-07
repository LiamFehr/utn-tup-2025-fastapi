# Autenticación JWT - Guía de Uso

## Endpoints Implementados

### 1. Registro de Usuario
**POST** `/auth/register`

```json
{
  "username": "testuser",
  "email": "test@example.com", 
  "password": "password123"
}
```

### 2. Login de Usuario  
**POST** `/auth/login`

```json
{
  "username": "testuser",
  "password": "password123"
}
```

**Respuesta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Login para Swagger UI
**POST** `/auth/login-form`
- Usa formulario OAuth2 compatible con Swagger UI

### 4. Información del Usuario Actual
**GET** `/auth/me`
- Requiere Bearer token
- Headers: `Authorization: Bearer <token>`

## Endpoints Protegidos (Requieren JWT)

### 1. Test de Autenticación
**GET** `/protected/test`
- Headers: `Authorization: Bearer <token>`

### 2. Perfil de Usuario
**GET** `/protected/user-profile`
- Headers: `Authorization: Bearer <token>`

### 3. Dashboard
**GET** `/protected/dashboard`
- Headers: `Authorization: Bearer <token>`

## Ejemplo de Uso con cURL

### 1. Registrar Usuario
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
  }'
```

### 2. Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser", 
    "password": "password123"
  }'
```

### 3. Acceder a Endpoint Protegido
```bash
# Reemplaza <TOKEN> con el token obtenido del login
curl -X GET "http://localhost:8000/protected/test" \
  -H "Authorization: Bearer <TOKEN>"
```

## Configuración

- **Duración del token**: 30 minutos (configurable en `auth.py`)
- **Algoritmo**: HS256
- **Secret Key**: Cambiar en producción (ver `auth.py`)

## Instalación de Dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar el Servidor

```bash
uvicorn main:app --reload
```

La documentación interactiva estará disponible en: http://localhost:8000/docs
