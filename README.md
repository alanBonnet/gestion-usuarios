# API-Gestion users
El siguiente repositorio contiene los servicios necesarios para el manejo de información que intervienen en un tramite digital.

## Instalación:

## Requisitos: (*)
- Tener instalado la versión de python del momento (3.12.4).

---
---
### Ejecutar los siguientes comandos:
---
- ### Para crear el entorno virtual: (*)
---
1. Con python por defecto usando un módulo que viene incluido en python 3:
```sh
python -m venv venv
```
---
- Para trabajar dentro del entorno virtual en una terminal ___CMD___:
  - Entrar a la siguiente ruta hasta estar al mismo nivel del archivo ___bat___
```sh
./venv/Scripts/activate.bat
```

Si está usando el terminal integrado de VS Code, se le pedirá reiniciarlo, y está listo.

---
---

### Instalación de dependencias: (*)
- Verificar primero si ya se está trabajando dentro del entorno virtual.
    - Aparece como un (venv':venv) en la barra de estados inferior de VS Code.
```sh
pip install -r requirements.txt
```
---
---

# Cargar los datos de la migracion y los Seeders
### Generación de las tablas según los modelos
```cmd
alembic revision --autogenerate
```
### Ejecución de las migraciones a la base de datos
```cmd
alembic upgrade head
```
### Ejecutar el Seed:
```cmd
python seeds_user.py
```
---
### Levantar el servidor: (*)
- En el archivo main está configurado para levantar en el puerto *`3002`*.
    - cambiar número de puerto según sea necesario.
```sh
python main.py
```
---
---
---
## A tener en cuenta (*):
- En el archivo `app/db` está una conexión a la base de datos local.
  - Su configuración está en `app/core/config.py` dentro de la lista `database_configs`, donde este mismo hace referencia a un `.env`, será necesario rellenar uno con los mismos, nombres o por lo menos pasarle los datos necesarios para la conexión local de desarrollo o producción, para eso está el archivo `.env.example` como guía.
  
  
  
  
