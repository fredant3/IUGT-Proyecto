# Esquema de Base de Datos SUCI

## Diagramas Entidad-Relación

### Módulo de Usuarios
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(254) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    first_name VARCHAR(150),
    last_name VARCHAR(150),
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_roles (
    user_id INTEGER REFERENCES users(id),
    role_id INTEGER REFERENCES roles(id),
    PRIMARY KEY (user_id, role_id)
);
```

### Módulo de RRHH
```sql
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_id INTEGER REFERENCES departments(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    department_id INTEGER REFERENCES departments(id),
    position VARCHAR(100),
    salary DECIMAL(10,2),
    hire_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employees(id),
    check_in TIMESTAMP,
    check_out TIMESTAMP,
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Módulo de Proyectos
```sql
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20),
    manager_id INTEGER REFERENCES employees(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(id),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    assignee_id INTEGER REFERENCES employees(id),
    due_date DATE,
    status VARCHAR(20),
    priority INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_members (
    project_id INTEGER REFERENCES projects(id),
    employee_id INTEGER REFERENCES employees(id),
    role VARCHAR(50),
    PRIMARY KEY (project_id, employee_id)
);
```

### Módulo de Documentos
```sql
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    file_path VARCHAR(500),
    file_type VARCHAR(50),
    file_size INTEGER,
    uploaded_by INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE document_permissions (
    document_id INTEGER REFERENCES documents(id),
    role_id INTEGER REFERENCES roles(id),
    permission_level VARCHAR(20),
    PRIMARY KEY (document_id, role_id)
);
```

### Módulo de Comunicaciones
```sql
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    sender_id INTEGER REFERENCES users(id),
    subject VARCHAR(200),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE message_recipients (
    message_id INTEGER REFERENCES messages(id),
    recipient_id INTEGER REFERENCES users(id),
    read_at TIMESTAMP,
    deleted_at TIMESTAMP,
    PRIMARY KEY (message_id, recipient_id)
);

CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title VARCHAR(200),
    content TEXT,
    type VARCHAR(50),
    read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Índices

### Índices de Búsqueda
```sql
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_employees_department ON employees(department_id);
CREATE INDEX idx_tasks_project ON tasks(project_id);
CREATE INDEX idx_tasks_assignee ON tasks(assignee_id);
```

### Índices de Tiempo
```sql
CREATE INDEX idx_projects_dates ON projects(start_date, end_date);
CREATE INDEX idx_tasks_due_date ON tasks(due_date);
CREATE INDEX idx_attendance_check ON attendance(check_in, check_out);
```

## Triggers

### Actualización de Timestamps
```sql
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_timestamp
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_timestamp();
```

### Logging de Cambios
```sql
CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY,
    table_name VARCHAR(50),
    record_id INTEGER,
    action VARCHAR(20),
    old_data JSONB,
    new_data JSONB,
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION audit_changes()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log (
        table_name,
        record_id,
        action,
        old_data,
        new_data,
        user_id
    ) VALUES (
        TG_TABLE_NAME,
        NEW.id,
        TG_OP,
        row_to_json(OLD),
        row_to_json(NEW),
        current_user_id()
    );
    RETURN NEW;
END;
$$ language 'plpgsql';
```

## Vistas

### Vista de Empleados
```sql
CREATE VIEW employee_details AS
SELECT 
    e.id,
    u.username,
    u.email,
    p.first_name,
    p.last_name,
    e.position,
    d.name as department,
    e.salary,
    e.hire_date
FROM 
    employees e
    JOIN users u ON e.user_id = u.id
    JOIN profiles p ON u.id = p.user_id
    JOIN departments d ON e.department_id = d.id
WHERE 
    u.is_active = true;
```

### Vista de Proyectos
```sql
CREATE VIEW project_summary AS
SELECT 
    p.id,
    p.name,
    p.status,
    p.start_date,
    p.end_date,
    COUNT(t.id) as total_tasks,
    SUM(CASE WHEN t.status = 'completed' THEN 1 ELSE 0 END) as completed_tasks,
    COUNT(DISTINCT pm.employee_id) as team_size
FROM 
    projects p
    LEFT JOIN tasks t ON p.id = t.project_id
    LEFT JOIN project_members pm ON p.id = pm.project_id
GROUP BY 
    p.id, p.name, p.status, p.start_date, p.end_date;
```

## Funciones

### Cálculo de Estadísticas
```sql
CREATE OR REPLACE FUNCTION calculate_department_stats(dept_id INTEGER)
RETURNS TABLE (
    total_employees INTEGER,
    avg_salary DECIMAL,
    total_salary DECIMAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        COUNT(*) as total_employees,
        AVG(salary) as avg_salary,
        SUM(salary) as total_salary
    FROM 
        employees
    WHERE 
        department_id = dept_id;
END;
$$ LANGUAGE plpgsql;
```

### Gestión de Permisos
```sql
CREATE OR REPLACE FUNCTION check_user_permission(
    user_id INTEGER,
    permission_name VARCHAR
) RETURNS BOOLEAN AS $$
DECLARE
    has_permission BOOLEAN;
BEGIN
    SELECT EXISTS (
        SELECT 1
        FROM user_roles ur
        JOIN role_permissions rp ON ur.role_id = rp.role_id
        JOIN permissions p ON rp.permission_id = p.id
        WHERE ur.user_id = check_user_permission.user_id
        AND p.name = permission_name
    ) INTO has_permission;
    
    RETURN has_permission;
END;
$$ LANGUAGE plpgsql;
```

## Constraints

### Validaciones de Datos
```sql
-- Validación de Email
ALTER TABLE users
ADD CONSTRAINT valid_email
CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$');

-- Validación de Fechas
ALTER TABLE projects
ADD CONSTRAINT valid_dates
CHECK (end_date >= start_date);

-- Validación de Salario
ALTER TABLE employees
ADD CONSTRAINT valid_salary
CHECK (salary >= 0);
```

### Unique Constraints
```sql
-- Prevenir duplicados en asignaciones
ALTER TABLE project_members
ADD CONSTRAINT unique_project_member
UNIQUE (project_id, employee_id);

-- Usuarios únicos por departamento
ALTER TABLE employees
ADD CONSTRAINT unique_user_per_department
UNIQUE (user_id, department_id);
```

## Mantenimiento

### Optimización
```sql
-- Actualizar estadísticas
ANALYZE users;
ANALYZE employees;
ANALYZE projects;

-- Limpiar registros obsoletos
DELETE FROM notifications 
WHERE created_at < NOW() - INTERVAL '30 days';

-- Vacuuming
VACUUM ANALYZE;
```

### Backup
```sql
-- Backup completo
pg_dump -U usuario -d base_datos -F c -b -v -f backup.sql

-- Backup de datos específicos
pg_dump -U usuario -d base_datos -t tabla --data-only -f datos_tabla.sql
```

## Seguridad

### Roles y Permisos
```sql
-- Crear roles
CREATE ROLE app_read;
CREATE ROLE app_write;

-- Asignar permisos
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_read;
GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_write;

-- Revocar permisos peligrosos
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM public;
```

### Encriptación
```sql
-- Habilitar extensión pgcrypto
CREATE EXTENSION pgcrypto;

-- Función para encriptar datos sensibles
CREATE OR REPLACE FUNCTION encrypt_sensitive_data(data TEXT)
RETURNS TEXT AS $$
BEGIN
    RETURN pgp_sym_encrypt(
        data,
        current_setting('app.encryption_key')
    );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
```