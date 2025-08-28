# Guía del Desarrollador SUCI

## Mixins y Clases Base

### BaseModelMixin
```python
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
```
Este mixin proporciona campos comunes para todos los modelos:
- `created_at`: Fecha y hora de creación (automática)
- `updated_at`: Fecha y hora de última actualización (automática)
- `deleted_at`: Fecha y hora de eliminación lógica
- `is_active`: Estado activo/inactivo del registro

#### Métodos Principales:
- `delete()`: Realiza eliminación lógica
- `hard_delete()`: Eliminación permanente del registro

### ControllerMixin
Implementa las vistas base para operaciones CRUD:

#### ListController
```python
class ListController(LoginRequiredMixin, ListView):
    def get_queryset(self):
        # Implementación de filtros y ordenamiento
    
    def get(self, request, *args, **kwargs):
        # Manejo de respuesta JSON para datatables
```

Características:
- Integración con DataTables
- Paginación automática
- Búsqueda y filtrado dinámico
- Ordenamiento por columnas

#### CreateController
```python
class CreateController(LoginRequiredMixin, CreateView):
    def post(self, request, *arg, **kwargs):
        # Validación y creación de registros
```

Funcionalidades:
- Validación automática de formularios
- Manejo de errores
- Respuestas JSON para AJAX
- Redirección configurable

### CrudMixin
Implementa la lógica de negocio para operaciones CRUD:

```python
class CrudService(ServiceUtilMixin):
    def getAll(self, start=0, length=10, search="", draw=0):
        # Obtención paginada de registros
    
    def creator(self, form, request, *arg, **kwargs):
        # Creación de registros con validación
```

Características:
- Búsqueda y filtrado avanzado
- Paginación de resultados
- Validación de datos
- Manejo de relaciones

## Patrones y Convenciones

### Estructura de Módulos
Cada módulo debe seguir esta estructura:
```
module_name/
├── __init__.py
├── admin.py
├── apps.py
├── models/
│   ├── __init__.py
│   └── entities.py
├── services/
│   ├── __init__.py
│   └── business_logic.py
├── controllers/
│   ├── __init__.py
│   └── views.py
└── tests/
    ├── __init__.py
    └── test_module.py
```

### Convenciones de Código

#### Nombres
- **Clases**: CamelCase
  ```python
  class UserProfile:
      pass
  ```
- **Métodos**: snake_case
  ```python
  def get_user_data():
      pass
  ```
- **Variables**: snake_case
  ```python
  user_count = 0
  ```

#### Docstrings
```python
def complex_function(param1, param2):
    """
    Descripción breve de la función.

    Args:
        param1 (tipo): Descripción del parámetro 1
        param2 (tipo): Descripción del parámetro 2

    Returns:
        tipo: Descripción del valor retornado

    Raises:
        ExceptionType: Descripción de cuándo se lanza
    """
    pass
```

## Mejores Prácticas

### Manejo de Errores
```python
try:
    result = some_operation()
except SpecificException as e:
    logger.error(f"Error en operación: {str(e)}")
    raise CustomException("Mensaje amigable")
```

### Validaciones
```python
def validate_data(data):
    if not isinstance(data, dict):
        raise ValidationError("Data debe ser un diccionario")
    
    required_fields = ['nombre', 'email']
    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Campo requerido: {field}")
```

### Logging
```python
import logging

logger = logging.getLogger(__name__)

def complex_operation():
    logger.info("Iniciando operación")
    try:
        # código
        logger.debug("Detalles de procesamiento")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
```

## Testing

### Unit Tests
```python
from django.test import TestCase

class UserServiceTest(TestCase):
    def setUp(self):
        # Configuración inicial
        
    def test_create_user(self):
        # Test específico
        
    def tearDown(self):
        # Limpieza
```

### Integration Tests
```python
class ApiIntegrationTest(TestCase):
    fixtures = ['test_data.json']
    
    def test_complete_workflow(self):
        # Test de flujo completo
```

## Seguridad

### Control de Acceso
```python
from django.contrib.auth.decorators import permission_required

@permission_required('app.view_model')
def protected_view(request):
    # Vista protegida
```

### Validación de Datos
```python
from django.core.validators import validate_email

def validate_user_input(data):
    validate_email(data['email'])
    if len(data['password']) < 8:
        raise ValidationError("Contraseña muy corta")
```

## Despliegue

### Configuración de Producción
```python
DEBUG = False
ALLOWED_HOSTS = ['dominio.com']
SECURE_SSL_REDIRECT = True
```

### Variables de Entorno
```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')
```

## Optimización

### Consultas a Base de Datos
```python
# Bueno
users = User.objects.select_related('profile').filter(active=True)

# Evitar
for user in users:
    print(user.profile.email)  # No genera consultas adicionales
```

### Caché
```python
from django.core.cache import cache

def get_expensive_data():
    data = cache.get('expensive_data')
    if data is None:
        data = expensive_calculation()
        cache.set('expensive_data', data, timeout=3600)
    return data
```