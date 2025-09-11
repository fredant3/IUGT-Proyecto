<h1 align="center" style="display: flex; align-items: center; justify-content: center; gap: 25px;">
  <img src="./suci/templates/static/img/logo.png" width="60" alt="S.U.C.I Logo">
  <i>(S.U.C.I)</i>
</h1>

<h1 align="center" style="margin-bottom: 0;">Sistema Unificado para el Control</h1>
<h1 align="center" style="margin-top: 0;">Interno del Ven911</h1>

## Paso 1

**Clonar el ropositorio**

```
git clone https://github.com/fredant3/IUGT-Proyecto.git
```

## Paso 2

**Ubicar la rama en la cual vas a desarrollar o ajustar (Modulo)**

```
# Para ver todas las ramas
git branch -a

# Cambiar o seleccionar la rama del modulo
git checkout <rama>
```

**Verificar que estas en la ultima version**

```
git pull origin main
```

## Paso 3

**Ejecutar el comando para recrear la carpeta venv (El entorno virtual)**
_Debes tener [instalando phyton](#instalando-phyton)_

```
python -m venv venv
```

## Paso 4

#### Activar el entorno virtual

```
# Windows
.\venv\Scripts\activate

# Linux y MacOS
source ./venv/bin/activate
```

_**Importante:** En el promp verifica que estas dentro del entorno virtual **(venv)**_
_(venv) prompt:~/suci$_

## Paso 5

#### Cambiarnos a la carpeta del proyecto (SUCI)

```
cd ./suci
```

## Paso 6

#### Instalar dependencias

```
pip install -r requirements.txt
si requiere postgre instalar psycopg2-binary
```

## Paso 7

#### Ejecutar las migraciones (Crear las tablas en la DB)

```
python manage.py migrate
```

## Paso 8

#### Crear un superusuario

```
python manage.py createsuperuser --user=26530315 --email=superuser@mail.com
```

#### Ejemplo: usuario de prueba

```
user: 26530315
email: superuser@mail.com
pass: asdzxc
```

## Paso 9

#### Iniciar la aplicacion

```
python manage.py runserver
```

## Instalar Phyton

**Windows:** _Descargar el instalador_
https://www.python.org/downloads/windows

**Linux:** _Ejecutar el comando_

```
sudo apt install python3
sudo apt install python3.11-venv
sudo apt install python3-pip
```

**MacOS:** _Ejecutar el comando_

```
brew install python3
```

## Extra

### Cuando se agrega una dependencia ejecutar

```
pip freeze > requirements.txt
```

### Cuando se modifique o se cree un modelo ejecutar

```
python manage.py makemigrations
```

### Packaging the Gestion Comunicacional Module

```
python ./gestion_comunicacional/setup.py sdist
```

**Eliminar las carpetas migraciones (PowerShell)**

```
Get-ChildItem -Recurse -Directory -Filter "migrations" | Remove-Item -Recurse -Force
```

**Migraciones**

```
python manage.py makemigrations helpers
python manage.py makemigrations users
python manage.py makemigrations dashboard
python manage.py makemigrations administracion

python manage.py makemigrations rrhh

python manage.py makemigrations tecnologia

```
