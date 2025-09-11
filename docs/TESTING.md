# Guía de Testing SUCI

## Estructura de Tests

### Organización de Archivos
```
tests/
├── unit/
│   ├── test_models.py
│   ├── test_services.py
│   └── test_validators.py
├── integration/
│   ├── test_apis.py
│   └── test_workflows.py
└── fixtures/
    └── test_data.json
```

## Tests Unitarios

### Modelos
```python
from django.test import TestCase
from apps.users.models import User

class UserModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com'
        }
        
    def test_create_user(self):
        user = User.objects.create(**self.user_data)
        self.assertEqual(user.username, self.user_data['username'])
        
    def test_user_str(self):
        user = User.objects.create(**self.user_data)
        self.assertEqual(str(user), self.user_data['username'])
```

### Servicios
```python
from django.test import TestCase
from apps.rrhh.services import EmpleadoService
from apps.rrhh.models import Empleado

class EmpleadoServiceTest(TestCase):
    def setUp(self):
        self.service = EmpleadoService()
        
    def test_calculate_antiguedad(self):
        empleado = Empleado.objects.create(
            fecha_ingreso='2020-01-01'
        )
        antiguedad = self.service.calculate_antiguedad(empleado)
        self.assertIsInstance(antiguedad, int)
```

### Validators
```python
from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.common.validators import validate_cedula

class ValidatorTest(TestCase):
    def test_cedula_validator(self):
        # Caso válido
        self.assertIsNone(validate_cedula('V12345678'))
        
        # Caso inválido
        with self.assertRaises(ValidationError):
            validate_cedula('12345')
```

## Tests de Integración

### APIs
```python
from rest_framework.test import APITestCase
from django.urls import reverse

class UserApiTest(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        self.url = reverse('user-list')
        
    def test_create_user_api(self):
        response = self.client.post(self.url, self.user_data)
        self.assertEqual(response.status_code, 201)
```

### Workflows
```python
from django.test import TestCase
from apps.planificacion.workflows import ProyectoWorkflow

class ProyectoWorkflowTest(TestCase):
    fixtures = ['test_data.json']
    
    def test_complete_workflow(self):
        workflow = ProyectoWorkflow()
        result = workflow.execute_complete_flow()
        self.assertTrue(result.success)
```

## Fixtures

### JSON Fixtures
```json
[
    {
        "model": "auth.user",
        "pk": 1,
        "fields": {
            "username": "testuser",
            "email": "test@example.com",
            "is_active": true
        }
    }
]
```

### Factory Boy
```python
import factory
from apps.users.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        
    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(
        lambda obj: f'{obj.username}@example.com'
    )
```

## Mocking

### Servicios Externos
```python
from unittest.mock import patch
from django.test import TestCase

class ExternalServiceTest(TestCase):
    @patch('services.external.ApiClient')
    def test_api_call(self, mock_client):
        mock_client.return_value.get_data.return_value = {
            'status': 'success'
        }
        # Test code here
```

### Datetime
```python
from unittest.mock import patch
from django.test import TestCase
from datetime import datetime

class TimeBasedTest(TestCase):
    @patch('django.utils.timezone.now')
    def test_time_calculation(self, mock_now):
        mock_now.return_value = datetime(2023, 1, 1)
        # Test code here
```

## Cobertura de Código

### Configuración
```ini
[run]
source = apps
omit = */migrations/*, */tests/*

[report]
exclude_lines =
    pragma: no cover
    def __str__
    pass
```

### Ejecución
```bash
coverage run manage.py test
coverage report
coverage html
```

## Tests de Rendimiento

### Load Testing
```python
from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 2)
    
    @task
    def list_users(self):
        self.client.get("/api/users/")
```

### Profiling
```python
import cProfile
import pstats

def profile_view(request):
    profiler = cProfile.Profile()
    profiler.enable()
    
    # View code here
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumtime')
    stats.print_stats()
```

## Continuous Integration

### GitHub Actions
```yaml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python manage.py test
```

## Mejores Prácticas

### Naming
```python
def test_should_create_user_when_valid_data():
    # Test code
    
def test_should_raise_error_when_invalid_email():
    # Test code
```

### Setup y Teardown
```python
class TestCase(TestCase):
    def setUp(self):
        # Create test data
        
    def tearDown(self):
        # Clean up
```

### Assertions
```python
def test_user_creation(self):
    user = User.objects.create(username='test')
    
    self.assertIsNotNone(user.id)
    self.assertEqual(user.username, 'test')
    self.assertTrue(user.is_active)
```

## Tips y Trucos

### Test Client
```python
from django.test import Client

def test_view(self):
    client = Client()
    response = client.get('/path/')
    self.assertEqual(response.status_code, 200)
```

### Temporary Files
```python
from django.core.files.uploadedfile import SimpleUploadedFile

def test_file_upload(self):
    file = SimpleUploadedFile(
        "file.txt",
        b"file_content"
    )
    response = self.client.post('/upload/', {'file': file})
```

### Signals
```python
from django.test import TestCase
from django.db.models.signals import post_save
from django.dispatch import receiver

class SignalTest(TestCase):
    def setUp(self):
        post_save.connect(receiver, sender=Model)
        
    def tearDown(self):
        post_save.disconnect(receiver, sender=Model)
```