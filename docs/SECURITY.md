# Guía de Seguridad SUCI

## Autenticación y Autorización

### Configuración de Autenticación
```python
# settings.py
AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'apps.security.backends.CustomAuthBackend',
)

# Configuración de sesiones
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
```

### Control de Acceso Basado en Roles (RBAC)
```python
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required

@permission_required('app.view_model')
def protected_view(request):
    # Vista protegida por permisos
    pass

@staff_member_required
def admin_view(request):
    # Vista solo para staff
    pass
```

### Middleware de Seguridad
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'apps.security.middleware.CustomSecurityMiddleware',
]
```

## Protección contra Ataques Comunes

### XSS (Cross-Site Scripting)
```python
# Template
{{ data|escape }}

# JavaScript
const safeHtml = DOMPurify.sanitize(unsafeHtml);
```

### CSRF (Cross-Site Request Forgery)
```python
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def my_view(request):
    # Vista protegida contra CSRF
    pass
```

### SQL Injection
```python
# Correcto
User.objects.filter(username=username)

# Incorrecto
User.objects.raw('SELECT * FROM users WHERE username = ' + username)
```

### Click-jacking
```python
# settings.py
X_FRAME_OPTIONS = 'DENY'

# O en templates específicos
@xframe_options_deny
def my_view(request):
    pass
```

## Gestión de Contraseñas

### Políticas de Contraseñas
```python
# settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 10,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'apps.security.validators.CustomPasswordValidator',
    },
]
```

### Almacenamiento Seguro
```python
from django.contrib.auth.hashers import make_password, check_password

# Hashear contraseña
password_hash = make_password(raw_password)

# Verificar contraseña
is_valid = check_password(raw_password, encoded_password)
```

## Seguridad en APIs

### Autenticación JWT
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# Configuración JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}
```

### Rate Limiting
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
```

## Encriptación de Datos

### En Base de Datos
```python
from django.db import models
from django_cryptography.fields import encrypt

class SensitiveData(models.Model):
    encrypted_field = encrypt(models.CharField(max_length=100))
```

### En Tránsito
```python
# settings.py
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

## Auditoría y Logging

### Configuración de Logs
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'security_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/suci/security.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'security': {
            'handlers': ['security_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### Registro de Eventos de Seguridad
```python
import logging

logger = logging.getLogger('security')

def login_view(request):
    if login_failed:
        logger.warning(
            'Failed login attempt',
            extra={
                'username': username,
                'ip': request.META.get('REMOTE_ADDR'),
                'user_agent': request.META.get('HTTP_USER_AGENT')
            }
        )
```

## Monitoreo de Seguridad

### Sistema de Detección de Intrusos (IDS)
```python
class SecurityMonitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Analizar patrones sospechosos
        if self._is_suspicious(request):
            self._log_suspicious_activity(request)
            return HttpResponseForbidden()
        return self.get_response(request)

    def _is_suspicious(self, request):
        patterns = [
            r'../|\.\.\\',  # Path traversal
            r'select.*from',  # SQL injection
            r'<script.*>',   # XSS
        ]
        # Implementar lógica de detección
        pass
```

## Respuesta a Incidentes

### Plan de Acción
1. Detección
2. Contención
3. Erradicación
4. Recuperación
5. Lecciones Aprendidas

### Procedimiento de Recuperación
```python
class IncidentResponse:
    @staticmethod
    def handle_breach(incident_type):
        # 1. Registrar incidente
        logger.critical(f'Security breach detected: {incident_type}')
        
        # 2. Notificar administradores
        notify_admins(incident_type)
        
        # 3. Activar modo seguro
        settings.MAINTENANCE_MODE = True
        
        # 4. Bloquear accesos sospechosos
        block_suspicious_ips()
        
        # 5. Iniciar recuperación
        start_recovery_procedure()
```

## Pruebas de Seguridad

### Tests Automatizados
```python
from django.test import TestCase
from django.urls import reverse

class SecurityTest(TestCase):
    def test_xss_protection(self):
        payload = '<script>alert("xss")</script>'
        response = self.client.post('/input/', {'data': payload})
        self.assertNotIn(payload, response.content.decode())

    def test_sql_injection_protection(self):
        payload = "' OR '1'='1"
        response = self.client.get(f'/users/?search={payload}')
        self.assertEqual(response.status_code, 400)
```

### Escaneo de Vulnerabilidades
```python
# requirements-security.txt
bandit==1.7.0
safety==1.10.3
```

## Configuración de Producción

### Headers de Seguridad
```nginx
# nginx configuration
add_header X-Content-Type-Options nosniff;
add_header X-Frame-Options DENY;
add_header X-XSS-Protection "1; mode=block";
add_header Content-Security-Policy "default-src 'self'";
add_header Referrer-Policy strict-origin-when-cross-origin;
```

### Firewall
```bash
# Configuración básica de UFW
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable
```

## Actualizaciones de Seguridad

### Proceso de Actualización
1. Monitorear alertas de seguridad
2. Evaluar impacto
3. Probar en ambiente de staging
4. Aplicar parches
5. Verificar funcionamiento

### Script de Actualización
```bash
#!/bin/bash
# security_update.sh

# Backup
./backup.sh

# Actualizar dependencias
pip install --upgrade -r requirements.txt

# Verificar vulnerabilidades conocidas
safety check

# Ejecutar tests
python manage.py test

# Reiniciar servicios
systemctl restart suci
```

## Referencias y Recursos

### Documentación Oficial
- [Django Security](https://docs.djangoproject.com/en/stable/topics/security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://www.sans.org/top25-software-errors/)

### Herramientas Recomendadas
- Django Security Middleware
- Python Safety
- Bandit
- OWASP ZAP
- Burp Suite