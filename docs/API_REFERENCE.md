# Referencia de API SUCI

## Autenticación

### Obtener Token
```http
POST /api/token/
Content-Type: application/json

{
    "username": "usuario",
    "password": "contraseña"
}
```

Respuesta:
```json
{
    "access": "token_jwt",
    "refresh": "refresh_token"
}
```

## Recursos

### Usuarios

#### Listar Usuarios
```http
GET /api/users/
Authorization: Bearer {token}
```

Parámetros de consulta:
- `page`: Número de página
- `size`: Registros por página
- `search`: Término de búsqueda
- `active`: Estado (true/false)

Respuesta:
```json
{
    "count": 100,
    "next": "url_siguiente_pagina",
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "usuario1",
            "email": "usuario1@ejemplo.com",
            "is_active": true
        }
    ]
}
```

#### Crear Usuario
```http
POST /api/users/
Authorization: Bearer {token}
Content-Type: application/json

{
    "username": "nuevo_usuario",
    "email": "nuevo@ejemplo.com",
    "password": "contraseña",
    "first_name": "Nombre",
    "last_name": "Apellido"
}
```

### Recursos Humanos

#### Listar Empleados
```http
GET /api/rrhh/empleados/
Authorization: Bearer {token}
```

#### Crear Empleado
```http
POST /api/rrhh/empleados/
Authorization: Bearer {token}
Content-Type: application/json

{
    "cedula": "V12345678",
    "nombres": "Juan",
    "apellidos": "Pérez",
    "fecha_ingreso": "2023-01-01",
    "cargo": "Analista",
    "departamento_id": 1
}
```

### Planificación

#### Listar Proyectos
```http
GET /api/planificacion/proyectos/
Authorization: Bearer {token}
```

#### Crear Proyecto
```http
POST /api/planificacion/proyectos/
Authorization: Bearer {token}
Content-Type: application/json

{
    "nombre": "Nuevo Proyecto",
    "descripcion": "Descripción del proyecto",
    "fecha_inicio": "2023-01-01",
    "fecha_fin": "2023-12-31",
    "responsable_id": 1
}
```

## Códigos de Estado

- 200: OK
- 201: Creado
- 400: Error de validación
- 401: No autorizado
- 403: Prohibido
- 404: No encontrado
- 500: Error interno del servidor

## Formatos de Respuesta

### Éxito
```json
{
    "status": "success",
    "data": {
        // Datos de respuesta
    }
}
```

### Error
```json
{
    "status": "error",
    "message": "Descripción del error",
    "errors": {
        // Detalles específicos del error
    }
}
```

## Paginación

La paginación se implementa mediante parámetros de consulta:
```http
GET /api/resource/?page=2&size=10
```

Respuesta:
```json
{
    "count": 100,
    "next": "/api/resource/?page=3&size=10",
    "previous": "/api/resource/?page=1&size=10",
    "results": []
}
```

## Filtrado

Los endpoints soportan filtrado mediante parámetros de consulta:
```http
GET /api/usuarios/?departamento=1&activo=true
```

## Ordenamiento

El ordenamiento se realiza mediante el parámetro `order`:
```http
GET /api/usuarios/?order=nombre,-fecha_ingreso
```

## Búsqueda

La búsqueda general se realiza mediante el parámetro `search`:
```http
GET /api/usuarios/?search=juan
```

## Rate Limiting

Las APIs tienen límites de uso:
- 1000 peticiones por hora para usuarios autenticados
- 100 peticiones por hora para usuarios no autenticados

## Versionado

El versionado se maneja mediante headers:
```http
Accept: application/json; version=1.0
```

## Webhooks

Los webhooks están disponibles para eventos importantes:
```http
POST /api/webhooks/configure/
Content-Type: application/json

{
    "url": "https://mi-servidor.com/webhook",
    "eventos": ["usuario.creado", "usuario.actualizado"]
}
```

## Errores Comunes

### 400 Bad Request
```json
{
    "status": "error",
    "message": "Datos inválidos",
    "errors": {
        "campo": ["Este campo es requerido"]
    }
}
```

### 401 Unauthorized
```json
{
    "status": "error",
    "message": "Token inválido o expirado"
}
```

### 403 Forbidden
```json
{
    "status": "error",
    "message": "No tiene permisos para realizar esta acción"
}
```

## Ejemplos de Uso

### Autenticación y Creación de Usuario
```python
import requests

# Obtener token
response = requests.post('https://api.suci.com/api/token/', 
    json={'username': 'usuario', 'password': 'contraseña'})
token = response.json()['access']

# Crear usuario
headers = {'Authorization': f'Bearer {token}'}
data = {
    'username': 'nuevo_usuario',
    'email': 'nuevo@ejemplo.com',
    'password': 'contraseña'
}
response = requests.post('https://api.suci.com/api/users/', 
    json=data, headers=headers)
```

### Listar y Filtrar Recursos
```python
# Listar empleados activos del departamento 1
params = {
    'departamento': 1,
    'activo': True,
    'page': 1,
    'size': 10
}
response = requests.get('https://api.suci.com/api/rrhh/empleados/', 
    params=params, headers=headers)
```