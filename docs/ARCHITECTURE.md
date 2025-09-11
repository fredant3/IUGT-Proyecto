# Arquitectura del Sistema SUCI

## Descripción General
SUCI es un sistema modular diseñado para gestionar diversos aspectos de la operación institucional. La arquitectura del sistema está basada en principios de diseño modernos y patrones de desarrollo robustos.

## Estructura del Proyecto
El proyecto está organizado en los siguientes módulos principales:

### Módulos Core
- **administracion**: Gestión administrativa del sistema

- **dashboard**: Panel de control principal

- **rrhh**: Recursos Humanos

- **users**: Gestión de usuarios

### Componentes Base
El sistema utiliza varios mixins y clases base que proporcionan funcionalidad común:

#### BaseModelMixin
Proporciona funcionalidad básica para todos los modelos, incluyendo:
- Gestión de fechas de creación y modificación
- Soft delete para mantener históricos
- Campos comunes como estado y observaciones

#### ControllerMixin
Implementa controladores base para operaciones CRUD:
- ListController: Vista de listados con paginación
- CreateController: Creación de registros
- UpdateController: Actualización de registros
- DeleteController: Eliminación de registros

#### CrudMixin
Servicios base para operaciones CRUD:
- Búsqueda y filtrado
- Creación y actualización de registros
- Validación de datos
- Gestión de respuestas

#### RepositoryMixin
Capa de acceso a datos con:
- Operaciones básicas de base de datos
- Manejo de consultas complejas
- Gestión de relaciones

#### ServiceUtilMixin
Utilidades comunes para servicios:
- Paginación de resultados
- Transformación de datos
- Manejo de respuestas API

## Patrones de Diseño
El sistema implementa varios patrones de diseño:
- **Repository Pattern**: Para abstracción de la capa de datos
- **Service Layer Pattern**: Para lógica de negocio
- **MVC/MVT**: Para la estructura general de la aplicación
- **Mixin Pattern**: Para compartir funcionalidad entre clases

## Flujo de Datos
1. El cliente hace una petición HTTP
2. El controlador apropiado procesa la petición
3. El servicio ejecuta la lógica de negocio
4. El repositorio gestiona las operaciones de base de datos
5. Los datos son transformados y devueltos al cliente

## Seguridad
- Autenticación basada en sesiones
- Control de acceso basado en roles
- Protección contra CSRF
- Validación de datos en múltiples niveles

## Convenciones de Código
- Se sigue PEP 8 para estilo de código Python
- Nombres de clases en CamelCase
- Nombres de métodos y variables en snake_case
- Documentación en español