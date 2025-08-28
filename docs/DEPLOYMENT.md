# Guía de Despliegue SUCI

## Entornos de Despliegue

### Desarrollo
- Servidor local para desarrollo
- Base de datos PostgreSQL local
- Debug activado
- Configuración de correo local

### Staging (Pruebas)
- Servidor de pruebas
- Base de datos de pruebas
- Datos de prueba
- Configuración similar a producción

### Producción
- Servidor de producción
- Base de datos de producción
- Optimizaciones activadas
- SSL/TLS habilitado

## Requisitos del Sistema

### Hardware Recomendado
- **CPU**: 4 cores mínimo
- **RAM**: 8GB mínimo
- **Almacenamiento**: 50GB mínimo
- **Red**: 100Mbps mínimo

### Software Necesario
- **Sistema Operativo**: Ubuntu 20.04 LTS o superior
- **Python**: 3.10 o superior
- **PostgreSQL**: 16 o superior
- **Nginx**: última versión estable
- **uWSGI**: última versión estable

## Preparación del Servidor

### Actualización del Sistema
```bash
sudo apt update
sudo apt upgrade -y
```

### Instalación de Dependencias
```bash
sudo apt install -y python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```

### Configuración de PostgreSQL
```bash
sudo -u postgres psql
CREATE DATABASE suci;
CREATE USER suci_user WITH PASSWORD 'password';
ALTER ROLE suci_user SET client_encoding TO 'utf8';
ALTER ROLE suci_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE suci_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE suci TO suci_user;
\q
```

## Configuración del Proyecto

### Variables de Entorno
Crear archivo `.env`:
```ini
DEBUG=False
ALLOWED_HOSTS=suci.dominio.com
DATABASE_URL=postgres://suci_user:password@localhost:5432/suci
SECRET_KEY=your-secret-key-here
STATIC_ROOT=/var/www/suci/static/
MEDIA_ROOT=/var/www/suci/media/
```

### Configuración de uWSGI
Archivo `uwsgi.ini`:
```ini
[uwsgi]
project = suci
base = /var/www

chdir = %(base)/%(project)
home = %(base)/%(project)/venv
module = %(project).wsgi:application

master = true
processes = 5
socket = %(base)/%(project)/%(project).sock
chmod-socket = 664
vacuum = true

die-on-term = true
```

### Configuración de Nginx
Archivo `/etc/nginx/sites-available/suci`:
```nginx
server {
    listen 80;
    server_name suci.dominio.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/suci;
    }

    location /media/ {
        root /var/www/suci;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/var/www/suci/suci.sock;
    }
}
```

## Proceso de Despliegue

### 1. Preparación del Código
```bash
# Clonar repositorio
git clone [URL_REPOSITORIO] /var/www/suci
cd /var/www/suci

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configuración de la Base de Datos
```bash
# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Colectar archivos estáticos
python manage.py collectstatic
```

### 3. Configuración del Servicio
Archivo `/etc/systemd/system/suci.service`:
```ini
[Unit]
Description=uWSGI instance to serve SUCI
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/suci
Environment="PATH=/var/www/suci/venv/bin"
ExecStart=/var/www/suci/venv/bin/uwsgi --ini uwsgi.ini

[Install]
WantedBy=multi-user.target
```

### 4. Iniciar Servicios
```bash
# Habilitar e iniciar servicios
sudo systemctl start suci
sudo systemctl enable suci
sudo systemctl restart nginx
```

## Monitoreo y Mantenimiento

### Logs
Configurar logging en `settings.py`:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/suci/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

### Backups
Script de backup `/etc/cron.daily/suci-backup`:
```bash
#!/bin/bash
DATE=$(date +%Y-%m-%d)
BACKUP_DIR=/var/backups/suci

# Backup de base de datos
pg_dump suci > $BACKUP_DIR/db_$DATE.sql

# Backup de archivos
tar -czf $BACKUP_DIR/files_$DATE.tar.gz /var/www/suci/media

# Eliminar backups antiguos (más de 30 días)
find $BACKUP_DIR -mtime +30 -delete
```

### Monitoreo
Configurar Prometheus y Grafana:

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'suci'
    static_configs:
      - targets: ['localhost:8000']
```

### Optimización de Rendimiento

#### Caché
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

#### Compresión Gzip
En nginx:
```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript text/xml;
```

## Seguridad

### SSL/TLS
Configurar Certbot:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d suci.dominio.com
```

### Firewall
```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

### Headers de Seguridad
En nginx:
```nginx
add_header X-Frame-Options "SAMEORIGIN";
add_header X-XSS-Protection "1; mode=block";
add_header X-Content-Type-Options "nosniff";
```

## Solución de Problemas

### Problemas Comunes

#### Error 502 Bad Gateway
1. Verificar estado de uWSGI:
```bash
sudo systemctl status suci
```

2. Revisar logs:
```bash
sudo tail -f /var/log/nginx/error.log
```

#### Problemas de Permisos
1. Verificar permisos:
```bash
sudo chown -R www-data:www-data /var/www/suci
sudo chmod -R 755 /var/www/suci
```

#### Problemas de Base de Datos
1. Verificar conexión:
```bash
psql -U suci_user -h localhost suci
```

## Actualizaciones

### Proceso de Actualización
```bash
cd /var/www/suci
source venv/bin/activate

# Pull cambios
git pull origin main

# Actualizar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Archivos estáticos
python manage.py collectstatic --noinput

# Reiniciar servicios
sudo systemctl restart suci
sudo systemctl restart nginx
```

### Rollback
```bash
# Volver a versión anterior
git checkout HEAD^

# Revertir migraciones si es necesario
python manage.py migrate [app] [previous_migration]

# Reiniciar servicios
sudo systemctl restart suci
```

## Integración Continua/Despliegue Continuo (CI/CD)

### GitHub Actions
```yaml
name: Deploy
on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Deploy to Server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /var/www/suci
            git pull origin main
            source venv/bin/activate
            pip install -r requirements.txt
            python manage.py migrate
            python manage.py collectstatic --noinput
            sudo systemctl restart suci
```