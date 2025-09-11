# Guía Rápida de Desarrollo SUCI

## Configuración en 5 Minutos

### 1. Clonar y Configurar
```bash
# Clonar repositorio
git clone git@github.com:fredant3/suci-ven911.git
cd suci-ven911

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con sus configuraciones
```

### 2. Preparar Base de Datos
```bash
# Crear base de datos
createdb suci

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser
```

### 3. Ejecutar Servidor
```bash
python manage.py runserver
```

## Estructura del Proyecto

```
suci/
├── apps/                    # Módulos de aplicación
│   ├── administracion/     # Gestión administrativa
│   ├── helpers/            # Utilidades comunes
│   └── users/             # Gestión de usuarios
├── suci/                   # Configuración principal
├── templates/              # Plantillas HTML
└── manage.py              # Script de gestión
```

## Ejemplos Rápidos

### Crear Nuevo Módulo
```bash
# Crear estructura básica
mkdir apps/mi_modulo
touch apps/mi_modulo/{__init__,admin,apps,models,views}.py

# Registrar en INSTALLED_APPS
# settings.py
INSTALLED_APPS += ['apps.mi_modulo']
```

### Modelo Básico
```python
# apps/mi_modulo/models.py
from apps.helpers.BaseModelMixin import BaseModel

class MiModelo(BaseModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
```

### Vista CRUD
```python
# apps/mi_modulo/views.py
from apps.helpers.ControllerMixin import ListController

class ListarRegistrosView(ListController):
    model = MiModelo
    template_name = 'mi_modulo/listar.html'
```

### URL
```python
# apps/mi_modulo/urls.py
from django.urls import path
from .views import ListarRegistrosView

urlpatterns = [
    path('listar/', ListarRegistrosView.as_view(), name='listar')
]
```

## Comandos Útiles

### Development
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Shell interactivo
python manage.py shell_plus

# Limpiar cache
python manage.py clear_cache
```

### Testing
```bash
# Ejecutar tests
python manage.py test

# Con coverage
coverage run manage.py test
coverage report
```

### Producción
```bash
# Recolectar estáticos
python manage.py collectstatic

# Comprobar configuración
python manage.py check --deploy
```

## Debugging

### Django Debug Toolbar
```python
# settings.py
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
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
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
```

## API Endpoints

### Autenticación
```http
POST /api/token/
Content-Type: application/json

{
    "username": "usuario",
    "password": "contraseña"
}
```

### Recursos
```http
GET /api/users/
Authorization: Bearer {token}
```

## Tips y Trucos

### VSCode Setup
```json
{
    "python.linting.enabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

### Git Hooks
```bash
# .git/hooks/pre-commit
#!/bin/sh
python manage.py test
```

## Flujo de Desarrollo

1. **Crear Branch**
```bash
git checkout -b feature/nueva-funcionalidad
```

2. **Implementar Cambios**
```bash
# Codificar
# Testear
# Documentar
```

3. **Commit**
```bash
git add .
git commit -m "feat: nueva funcionalidad"
```

4. **Pull Request**
- Crear PR en GitHub
- Esperar revisión
- Merge a main

## Recursos

### Documentación
- [Django Docs](https://docs.djangoproject.com/)
- [DRF Docs](https://www.django-rest-framework.org/)
- [Documentación SUCI](docs/)

### Herramientas
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)
- [Coverage.py](https://coverage.readthedocs.io/)
- [Black](https://black.readthedocs.io/)

### Comunidad
- GitHub Issues
- Stack Overflow
- Discord

## Checklist de Desarrollo

### Nueva Funcionalidad
- [ ] Crear branch
- [ ] Implementar modelos
- [ ] Crear migraciones
- [ ] Implementar vistas
- [ ] Agregar tests
- [ ] Documentar
- [ ] Pull request

### Despliegue
- [ ] Ejecutar tests
- [ ] Actualizar dependencias
- [ ] Aplicar migraciones
- [ ] Recolectar estáticos
- [ ] Verificar logs

## Soporte

### Reportar Bugs
1. Verificar si existe el issue
2. Crear nuevo issue con:
   - Descripción
   - Pasos para reproducir
   - Comportamiento esperado
   - Logs relevantes

### Contribuir
1. Fork repository
2. Crear branch
3. Implementar cambios
4. Crear pull request

## Notas Importantes

### Seguridad
- No commitear .env
- Usar variables de entorno
- Validar entradas
- Escapar salidas

### Performance
- Usar select_related()
- Implementar caché
- Optimizar queries
- Paginar resultados

### Buenas Prácticas
- Seguir PEP 8
- Documentar código
- Escribir tests
- Usar tipos estáticos
