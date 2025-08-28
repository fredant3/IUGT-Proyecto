# Guía de Instalación y Configuración de SUCI

## Requisitos Previos
### Python
- Windows: [Descargar el instalador de Python](https://www.python.org/downloads/)
- Linux/Unix: Python suele venir preinstalado
- Versión recomendada: Python 3.13 o superior

### Base de Datos
- PostgreSQL 16 o superior
- Crear una base de datos para el proyecto

## Proceso de Instalación

### 1. Clonar el Repositorio
```bash
git clone git@github.com:fredant3/suci-ven911.git
cd suci
```

### 2. Gestión de Ramas
- Identificar la rama correspondiente a tu módulo
- Crear una nueva rama si es necesario:
```bash
git checkout -b feature/[nombre-funcionalidad]
```

### 3. Entorno Virtual
Crear y activar el entorno virtual:

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/Unix
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### 5. Configuración del Proyecto
1. Copiar el archivo .env.example a .env
2. Configurar las variables de entorno en .env:
   - DATABASE_URL
   - SECRET_KEY
   - DEBUG
   - Otras configuraciones específicas

### 6. Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear Superusuario
```bash
python manage.py createsuperuser
```

### 8. Ejecutar el Servidor de Desarrollo
```bash
python manage.py runserver
```

## Mantenimiento

### Actualización de Dependencias
Cuando se agreguen nuevas dependencias:
```bash
pip freeze > requirements.txt
```

### Gestión de Módulos
Para empaquetar módulos específicos (ejemplo: Gestión Comunicacional):
```bash
python -m build
```

## Solución de Problemas Comunes

### Error de Conexión a Base de Datos
1. Verificar credenciales en .env
2. Confirmar que el servicio de base de datos esté activo
3. Comprobar permisos de usuario

### Problemas con el Entorno Virtual
1. Verificar activación del entorno
2. Reinstalar en caso de problemas:
```bash
rm -rf venv
python -m venv venv
```

### Errores de Migración
1. Eliminar archivos de migración (si es seguro hacerlo)
2. Recrear migraciones desde cero
3. Aplicar migraciones en orden

## Recomendaciones de Desarrollo
- Mantener actualizado el entorno virtual
- Seguir las convenciones de código del proyecto
- Documentar cambios significativos
- Realizar pruebas antes de commit