# Estándares de Código SUCI

## Guía de Estilo

### 1. Convenciones de Nomenclatura

#### Clases
```python
# Correcto
class UserProfile:
    pass

class HTTPResponse:
    pass

# Incorrecto
class userProfile:
    pass

class Http_Response:
    pass
```

#### Funciones y Variables
```python
# Correcto
def calculate_total():
    pass

user_count = 0
first_name = "Juan"

# Incorrecto
def calculateTotal():
    pass

userCount = 0
firstName = "Juan"
```

#### Constantes
```python
# Correcto
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# Incorrecto
maxConnections = 100
default_timeout = 30
apiBaseUrl = "https://api.example.com"
```

### 2. Estructura de Código

#### Imports
```python
# Correcto
from django.db import models
from django.contrib.auth.models import User
from .models import Profile
from third_party import ThirdPartyClass
import local_module

# Incorrecto
from django.db.models import *
import django, sys, os
from .models import *
```

#### Organización de Clases
```python
class UserService:
    """Servicio para gestión de usuarios."""
    
    # 1. Constantes de clase
    DEFAULT_AGE = 18
    
    # 2. Métodos dunder/mágicos
    def __init__(self):
        self.users = []
    
    # 3. Propiedades
    @property
    def active_users(self):
        return [u for u in self.users if u.is_active]
    
    # 4. Métodos públicos
    def create_user(self, data):
        pass
    
    # 5. Métodos protegidos
    def _validate_data(self, data):
        pass
    
    # 6. Métodos privados
    def __clean_input(self, value):
        pass
```

### 3. Docstrings y Comentarios

#### Documentación de Módulos
```python
"""
Este módulo proporciona funcionalidad para la gestión de usuarios.

Incluye clases y funciones para:
- Creación y actualización de usuarios
- Validación de datos
- Gestión de permisos
"""

from django.db import models
```

#### Documentación de Clases
```python
class UserManager:
    """
    Gestor de operaciones relacionadas con usuarios.
    
    Attributes:
        users (list): Lista de usuarios activos
        max_users (int): Límite máximo de usuarios
    
    Note:
        Esta clase maneja toda la lógica de negocio relacionada
        con la gestión de usuarios.
    """
```

#### Documentación de Métodos
```python
def validate_user_data(data: dict) -> bool:
    """
    Valida los datos de usuario antes de su creación.

    Args:
        data (dict): Diccionario con datos del usuario
            - username (str): Nombre de usuario
            - email (str): Correo electrónico
            - age (int): Edad del usuario

    Returns:
        bool: True si los datos son válidos, False en caso contrario

    Raises:
        ValueError: Si faltan campos requeridos
        ValidationError: Si los datos no cumplen el formato
    """
```

### 4. Manejo de Errores

#### Try-Except
```python
# Correcto
try:
    user = User.objects.get(id=user_id)
except User.DoesNotExist:
    logger.error(f"Usuario {user_id} no encontrado")
    raise CustomUserError("Usuario no encontrado")
except Exception as e:
    logger.critical(f"Error inesperado: {str(e)}")
    raise

# Incorrecto
try:
    user = User.objects.get(id=user_id)
except:  # Muy general
    print("Error")
```

#### Custom Exceptions
```python
class CustomUserError(Exception):
    """Excepción base para errores de usuario."""
    pass

class UserNotFoundError(CustomUserError):
    """Se lanza cuando no se encuentra un usuario."""
    pass

class UserValidationError(CustomUserError):
    """Se lanza cuando los datos del usuario son inválidos."""
    pass
```

### 5. Testing

#### Organización de Tests
```python
from django.test import TestCase

class UserServiceTest(TestCase):
    """Tests para el servicio de usuarios."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.service = UserService()
    
    def test_create_user_success(self):
        """Test de creación exitosa de usuario."""
        result = self.service.create_user(valid_data)
        self.assertTrue(result.success)
    
    def test_create_user_invalid_data(self):
        """Test de creación con datos inválidos."""
        with self.assertRaises(UserValidationError):
            self.service.create_user(invalid_data)
```

### 6. Optimización y Rendimiento

#### Queries de Base de Datos
```python
# Correcto
users = User.objects.select_related('profile')\
              .prefetch_related('groups')\
              .filter(is_active=True)

for user in users:
    print(user.profile.email)  # No genera queries adicionales

# Incorrecto
users = User.objects.filter(is_active=True)
for user in users:
    print(user.profile.email)  # N+1 queries
```

#### Uso de Cache
```python
from django.core.cache import cache

def get_user_stats(user_id):
    cache_key = f'user_stats_{user_id}'
    stats = cache.get(cache_key)
    
    if stats is None:
        stats = calculate_user_stats(user_id)
        cache.set(cache_key, stats, timeout=3600)
    
    return stats
```

### 7. Seguridad

#### Validación de Entrada
```python
def process_user_data(data):
    """Procesa datos de usuario con validación."""
    if not isinstance(data, dict):
        raise ValueError("Data debe ser un diccionario")
    
    required = ['username', 'email']
    if not all(key in data for key in required):
        raise ValueError("Faltan campos requeridos")
    
    # Sanitización
    data['username'] = bleach.clean(data['username'])
    data['email'] = bleach.clean(data['email'])
    
    return data
```

#### Manejo de Datos Sensibles
```python
from django.conf import settings
from cryptography.fernet import Fernet

def encrypt_sensitive_data(data: str) -> str:
    """Encripta datos sensibles."""
    f = Fernet(settings.ENCRYPTION_KEY)
    return f.encrypt(data.encode()).decode()

def decrypt_sensitive_data(encrypted_data: str) -> str:
    """Desencripta datos sensibles."""
    f = Fernet(settings.ENCRYPTION_KEY)
    return f.decrypt(encrypted_data.encode()).decode()
```

### 8. Logging

#### Configuración de Logs
```python
import logging

logger = logging.getLogger(__name__)

def complex_operation():
    """Operación con logging detallado."""
    logger.info("Iniciando operación compleja")
    try:
        result = perform_operation()
        logger.debug(f"Resultado: {result}")
        return result
    except Exception as e:
        logger.error(f"Error en operación: {str(e)}", exc_info=True)
        raise
```

### 9. Documentación de API

#### Decoradores de API
```python
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    operation_description="Crea un nuevo usuario",
    request_body=UserSerializer,
    responses={201: UserSerializer}
)
@api_view(['POST'])
def create_user(request):
    """
    Endpoint para crear usuarios.
    
    Request:
        - username: string
        - email: string
        - password: string
    
    Response:
        - id: integer
        - username: string
        - email: string
    """
    pass
```

### 10. Versionamiento

#### Control de Versiones
```python
# version.py
VERSION = (2, 1, 0)  # Major, Minor, Patch

def get_version():
    """Obtiene la versión actual del sistema."""
    return '.'.join(str(v) for v in VERSION)
```

### 11. Configuración

#### Manejo de Settings
```python
# settings.py
from decouple import config

# Configuración de Base de Datos
DATABASE_URL = config('DATABASE_URL')
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')

# Configuración de Email
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
```

### 12. Rendimiento

#### Optimización de Memoria
```python
def process_large_dataset(data_generator):
    """Procesa grandes conjuntos de datos de forma eficiente."""
    result = []
    for chunk in data_generator:
        processed = process_chunk(chunk)
        result.extend(processed)
        # Liberar memoria
        del chunk
    return result

def data_generator(file_path):
    """Generador para procesar archivos grandes."""
    with open(file_path) as f:
        for line in f:
            yield process_line(line)
```

### 13. Git

#### Mensajes de Commit
```
# Formato recomendado:
# <tipo>(<alcance>): <descripción>
#
# <cuerpo>
#
# <pie>

# Ejemplos:
feat(users): implementar autenticación con JWT

fix(api): corregir error en validación de datos

docs(readme): actualizar instrucciones de instalación
```

### 14. Manejo de Archivos

#### Operaciones con Archivos
```python
def safe_file_handling(file_path):
    """Manejo seguro de archivos."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        logger.error(f"Archivo no encontrado: {file_path}")
        raise
    except IOError as e:
        logger.error(f"Error de I/O: {str(e)}")
        raise
```