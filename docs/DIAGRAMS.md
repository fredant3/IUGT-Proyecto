# Diagramas del Sistema SUCI

## Arquitectura General

```mermaid
graph TB
    subgraph Frontend
        UI[Interfaz de Usuario]
        JS[JavaScript/Ajax]
        Templates[Templates Django]
    end

    subgraph Backend
        Views[Vistas/Controladores]
        Services[Servicios]
        Repos[Repositorios]
        Models[Modelos]
    end

    subgraph Infrastructure
        DB[(Base de Datos)]
        Cache[(Cache Redis)]
        Static[Archivos Estáticos]
    end

    UI --> JS
    JS --> Views
    Templates --> Views
    Views --> Services
    Services --> Repos
    Repos --> Models
    Models --> DB
    Services --> Cache
```

## Flujo de Autenticación

```mermaid
sequenceDiagram
    participant U as Usuario
    participant F as Frontend
    participant A as Auth Service
    participant D as Database

    U->>F: Ingresar Credenciales
    F->>A: POST /api/login
    A->>D: Verificar Credenciales
    D-->>A: Usuario Válido
    A-->>F: Token JWT
    F-->>U: Redirigir a Dashboard
```

## Estructura de Módulos

```mermaid
graph LR
    subgraph Core
        Base[BaseModule]
        Auth[Authentication]
        Perms[Permissions]
    end

    subgraph Business
        HR[RRHH]
        Fin[Finanzas]
        Inv[Inventario]
    end

    subgraph Support
        Log[Logging]
        Cache[Caching]
        Utils[Utilities]
    end

    Core --> Business
    Support --> Business
    Support --> Core
```

## Flujo CRUD

```mermaid
sequenceDiagram
    participant C as Cliente
    participant V as Vista
    participant S as Servicio
    participant R as Repositorio
    participant D as Base de Datos

    C->>V: Request
    V->>S: Procesar Request
    S->>R: Operación CRUD
    R->>D: Query
    D-->>R: Resultado
    R-->>S: Datos
    S-->>V: Respuesta Formateada
    V-->>C: Response
```

## Modelo de Datos

```mermaid
erDiagram
    USUARIO ||--o{ PERFIL : tiene
    USUARIO ||--o{ ROL : asignado
    DEPARTAMENTO ||--o{ EMPLEADO : contiene
    EMPLEADO ||--o{ PROYECTO : participa
    PROYECTO ||--o{ TAREA : contiene
    
    USUARIO {
        int id
        string username
        string email
        boolean is_active
    }
    
    PERFIL {
        int id
        string nombre
        string apellido
        date fecha_nacimiento
    }
    
    DEPARTAMENTO {
        int id
        string nombre
        string descripcion
    }
    
    EMPLEADO {
        int id
        string cedula
        string cargo
        date fecha_ingreso
    }
    
    PROYECTO {
        int id
        string nombre
        date fecha_inicio
        date fecha_fin
    }
```

## Arquitectura de Microservicios

```mermaid
graph TB
    subgraph "Gateway API"
        GW[API Gateway]
    end

    subgraph "Servicios Core"
        Auth[Autenticación]
        Users[Usuarios]
        Perms[Permisos]
    end

    subgraph "Servicios de Negocio"
        HR[RRHH]
        Finance[Finanzas]
        Projects[Proyectos]
    end

    subgraph "Servicios de Soporte"
        Email[Email]
        Storage[Almacenamiento]
        Cache[Cache]
    end

    GW --> Auth
    GW --> Users
    GW --> HR
    GW --> Finance
    GW --> Projects
    
    Auth --> Cache
    Users --> Storage
    HR --> Email
```

## Proceso de CI/CD

```mermaid
graph LR
    subgraph "Desarrollo"
        Code[Código]
        Test[Pruebas]
    end

    subgraph "Integración"
        Build[Build]
        QA[Quality Assurance]
    end

    subgraph "Despliegue"
        Stage[Staging]
        Prod[Producción]
    end

    Code --> Test
    Test --> Build
    Build --> QA
    QA --> Stage
    Stage --> Prod
```

## Sistema de Cache

```mermaid
graph TB
    subgraph "Cliente"
        Browser[Navegador]
        LocalS[Local Storage]
    end

    subgraph "Servidor"
        View[Vista]
        Cache[Redis Cache]
        DB[(Base de Datos)]
    end

    Browser --> LocalS
    Browser --> View
    View --> Cache
    Cache --> DB
```

## Manejo de Sesiones

```mermaid
stateDiagram-v2
    [*] --> Login
    Login --> Autenticado
    Autenticado --> Activo
    Activo --> Inactivo: Timeout
    Inactivo --> Login: Relogin
    Activo --> [*]: Logout
```

## Flujo de Notificaciones

```mermaid
graph TB
    subgraph "Eventos"
        E1[Usuario Creado]
        E2[Tarea Asignada]
        E3[Proyecto Actualizado]
    end

    subgraph "Procesamiento"
        Queue[Cola de Mensajes]
        Worker[Worker]
    end

    subgraph "Notificación"
        Email[Email]
        Push[Push Notification]
        Internal[Notificación Interna]
    end

    E1 & E2 & E3 --> Queue
    Queue --> Worker
    Worker --> Email & Push & Internal
```

## Arquitectura de Seguridad

```mermaid
graph TB
    subgraph "Capas de Seguridad"
        FW[Firewall]
        WAF[Web Application Firewall]
        Auth[Autenticación]
        Perm[Permisos]
        Enc[Encriptación]
    end

    subgraph "Datos Sensibles"
        PII[Información Personal]
        Cred[Credenciales]
        Docs[Documentos]
    end

    Internet --> FW
    FW --> WAF
    WAF --> Auth
    Auth --> Perm
    Perm --> Enc
    Enc --> PII & Cred & Docs
```

## Sistema de Logs

```mermaid
graph TB
    subgraph "Fuentes"
        App[Aplicación]
        DB[Base de Datos]
        Sys[Sistema]
    end

    subgraph "Procesamiento"
        Col[Colector]
        Parser[Parser]
        Filter[Filtro]
    end

    subgraph "Almacenamiento"
        ES[Elasticsearch]
        S3[Almacenamiento S3]
    end

    subgraph "Visualización"
        Kibana[Kibana]
        Grafana[Grafana]
    end

    App & DB & Sys --> Col
    Col --> Parser
    Parser --> Filter
    Filter --> ES & S3
    ES --> Kibana & Grafana
```

## Integración de Servicios

```mermaid
graph TB
    subgraph "SUCI Core"
        API[API Gateway]
        Auth[Autenticación]
        DB[(Base de Datos)]
    end

    subgraph "Servicios Externos"
        Email[Servidor Email]
        SMS[Servicio SMS]
        Storage[Almacenamiento Cloud]
    end

    subgraph "Integraciones"
        Payment[Pasarela de Pago]
        CRM[Sistema CRM]
        ERP[Sistema ERP]
    end

    API --> Auth
    Auth --> DB
    API --> Email & SMS & Storage
    API --> Payment & CRM & ERP
```

## Sistema de Reportes

```mermaid
graph TB
    subgraph "Datos"
        DB[(Base de Datos)]
        Cache[(Cache)]
    end

    subgraph "Procesamiento"
        Engine[Motor de Reportes]
        Queue[Cola de Trabajos]
        Worker[Worker]
    end

    subgraph "Formatos"
        PDF[PDF]
        Excel[Excel]
        CSV[CSV]
    end

    DB --> Cache
    Cache --> Engine
    Engine --> Queue
    Queue --> Worker
    Worker --> PDF & Excel & CSV
```