# Guía de Solución de Problemas SUCI

## Problemas Comunes y Soluciones

### 1. Errores de Instalación

#### Python/Virtualenv
```
Error: Command 'python' not found
```
**Solución:**
```bash
# Ubuntu/Debian
sudo apt install python3 python3-venv

# Windows
# Descargar e instalar Python desde python.org
```

#### Dependencias
```
Error: Could not find a version that satisfies the requirement
```
**Solución:**
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Limpiar cache
pip cache purge

# Reinstalar dependencias
pip install -r requirements.txt
```

### 2. Errores de Base de Datos

#### Conexión
```
django.db.utils.OperationalError: could not connect to server
```
**Solución:**
1. Verificar servicio PostgreSQL:
```bash
sudo systemctl status postgresql
```

2. Verificar credenciales en `.env`:
```
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

#### Migraciones
```
django.db.utils.ProgrammingError: relation "table_name" does not exist
```
**Solución:**
```bash
# Resetear migraciones
python manage.py migrate --fake zero
python manage.py migrate --fake-initial

# O crear nuevas migraciones
python manage.py makemigrations
python manage.py migrate
```

### 3. Errores en Tiempo de Ejecución

#### ModuleNotFoundError
```
ModuleNotFoundError: No module named 'module_name'
```
**Solución:**
1. Verificar entorno virtual:
```bash
which python
# Debe mostrar el path del virtualenv
```

2. Verificar PYTHONPATH:
```bash
export PYTHONPATH=$PYTHONPATH:/path/to/project
```

#### TemplateDoesNotExist
```
TemplateDoesNotExist at /path/
```
**Solución:**
1. Verificar configuración de templates:
```python
# settings.py
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
]
```

2. Verificar estructura de directorios:
```bash
ls templates/
# Verificar que el template existe
```

### 4. Errores de Permisos

#### Media/Static Files
```
PermissionError: [Errno 13] Permission denied
```
**Solución:**
```bash
# Ajustar permisos
sudo chown -R www-data:www-data /var/www/suci/media
sudo chmod -R 755 /var/www/suci/media
```

#### Logs
```
PermissionError: [Errno 13] Permission denied: '/var/log/suci/app.log'
```
**Solución:**
```bash
sudo mkdir -p /var/log/suci
sudo chown -R www-data:www-data /var/log/suci
sudo chmod 755 /var/log/suci
```

### 5. Errores de Rendimiento

#### Consultas Lentas
**Síntoma:** Páginas cargan lentamente

**Solución:**
1. Usar Django Debug Toolbar:
```python
INSTALLED_APPS += ['debug_toolbar']

# Optimizar consultas
Model.objects.select_related('foreign_key')
```

2. Configurar caché:
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

#### Memoria Alta
**Síntoma:** `MemoryError` o servidor lento

**Solución:**
1. Ajustar configuración de uWSGI:
```ini
[uwsgi]
memory-report = true
max-requests = 1000
reload-on-rss = 200
```

2. Monitorear uso de memoria:
```bash
ps aux | grep uwsgi
```

### 6. Errores de Despliegue

#### Error 502 Bad Gateway
**Solución:**
1. Verificar logs:
```bash
sudo tail -f /var/log/nginx/error.log
```

2. Verificar socket uWSGI:
```bash
# Verificar permisos
ls -l /var/www/suci/suci.sock

# Reiniciar servicios
sudo systemctl restart suci nginx
```

#### Static Files No Sirven
**Solución:**
1. Verificar configuración:
```python
STATIC_ROOT = '/var/www/suci/static/'
STATIC_URL = '/static/'
```

2. Recolectar archivos:
```bash
python manage.py collectstatic --noinput
```

### 7. Errores de Autenticación

#### No se Puede Iniciar Sesión
**Solución:**
1. Verificar configuración:
```python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
```

2. Resetear contraseña:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username='usuario')
user.set_password('nueva_contraseña')
user.save()
```

### 8. Errores de Código

#### ImportError Circular
```
ImportError: cannot import name 'X' from partially initialized module 'Y'
```
**Solución:**
1. Mover imports:
```python
# Antes del error
from .models import MyModel

# Después del error (dentro de la función)
def my_function():
    from .models import MyModel
```

#### ValidationError
```
django.core.exceptions.ValidationError
```
**Solución:**
1. Debugging con iPython:
```python
from IPython import embed; embed()
```

2. Verificar datos:
```python
try:
    instance.full_clean()
except ValidationError as e:
    print(e.message_dict)
```

## Herramientas de Diagnóstico

### Django Debug Toolbar
```python
# settings.py
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1']
```

### Logging
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': '/var/log/suci/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    },
}
```

### Profiling
```python
import cProfile
import pstats

def profile_view(request):
    with cProfile.Profile() as pr:
        # View code here
        
    stats = pstats.Stats(pr)
    stats.sort_stats('cumtime')
    stats.print_stats(20)
```

## Mantenimiento Preventivo

### Checklist Diario
1. Verificar logs de errores
2. Monitorear uso de recursos
3. Verificar backups
4. Revisar métricas de rendimiento

### Checklist Semanal
1. Actualizar dependencias
2. Realizar pruebas de integración
3. Revisar alertas de seguridad
4. Limpiar archivos temporales

### Checklist Mensual
1. Análisis de rendimiento
2. Revisión de código
3. Actualización de documentación
4. Pruebas de recuperación

## Scripts de Utilidad

### Verificar Estado del Sistema
```python
# health_check.py
import psutil
import django
from django.db import connections

def check_system_health():
    # CPU y memoria
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    
    # Base de datos
    db_ok = all(conn.is_usable() for conn in connections.all())
    
    return {
        'cpu_usage': cpu_percent,
        'memory_usage': memory.percent,
        'database_ok': db_ok,
    }
```

### Limpiar Datos Temporales
```python
# cleanup.py
from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.db.models import Q
import datetime

class Command(BaseCommand):
    help = 'Limpia datos temporales y caché'

    def handle(self, *args, **options):
        # Limpiar caché
        cache.clear()
        
        # Limpiar sesiones expiradas
        Session.objects.filter(
            expire_date__lt=datetime.now()
        ).delete()
        
        # Limpiar archivos temporales
        TempFile.objects.filter(
            created_at__lt=datetime.now() - timedelta(days=7)
        ).delete()
```

## Contacto y Soporte

### Niveles de Soporte
1. **Nivel 1**: Soporte básico
   - Problemas de acceso
   - Errores comunes
   - Consultas generales

2. **Nivel 2**: Soporte técnico
   - Problemas de configuración
   - Errores de sistema
   - Optimización

3. **Nivel 3**: Desarrollo
   - Bugs
   - Nuevas funcionalidades
   - Cambios mayores

### Proceso de Escalamiento
1. Documentar el problema
2. Recolectar logs relevantes
3. Crear ticket en sistema de seguimiento
4. Asignar al nivel apropiado
5. Seguimiento hasta resolución

### Información Requerida
- Descripción detallada del error
- Pasos para reproducir
- Logs relevantes
- Capturas de pantalla
- Ambiente (desarrollo/producción)