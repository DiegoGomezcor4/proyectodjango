# Proyecto Integrador Grupal: E-COMMERCE DJANGO MARKET
## Codo a Codo 4.0 - Django - Comisión #23654

GRUPO 6:
+ Diego Gomez - diegocor4@gmail.com
+ Ronald Palacios - rpalacioso12@gmail.com
+ Lorena Fracchia - lorenamfra@gmail.com 
+ Ezequiel Alejandro Acevedo

#
### Estructura del proyecto
```text 
\---proyectodjango
    |   .env
    |   .gitignore
    |   db.sqlite3
    |   manage.py
    |   README.md
    |   requirements.txt
    |   
    +---.vscode
    |       settings.json
    |       
    +---carrito
    |   |   admin.py
    |   |   apps.py
    |   |   models.py
    |   |   tests.py
    |   |   url.py
    |   |   views.py
    |   |   __init__.py
    |   |   
    |   +---migrations
    |   |   |   __init__.py
    |   |   |   
    |   |   \---__pycache__
    |   |           __init__.cpython-311.pyc
    |   |           
    |   \---__pycache__
    |           
    +---core
    |   |   admin.py
    |   |   apps.py
    |   |   forms.py
    |   |   models.py
    |   |   tests.py
    |   |   views.py
    |   |   __init__.py
    |   |   
    |   +---migrations
    |   |   |   0001_initial.py
    |   |   |   __init__.py
    |   |   |   
    |   |   \---__pycache__
    |   |           
    |   +---static
    |   |   +---css
    |   |   |       bootstrap.min.css
    |   |   |       bootstrap.min.css.map
    |   |   |       contact.css
    |   |   |       home.css
    |   |   |       login_admin.css
    |   |   |       productos_listado.css
    |   |   |       signup.css
    |   |   |       style.css
    |   |   |       usuarios_listado.css
    |   |   |       
    |   |   +---img
    |   |   |   +---cards
    |   |   |   +---carrousel
    |   |   |   \---products
    |   |   |           
    |   |   \---js
    |   +---templates
    |   |       carrito.html
    |   |       contact.html
    |   |       home.html
    |   |       login.html
    |   |       login_admin.html
    |   |       logout_admin.html
    |   |       master.html
    |   |       product.html
    |   |       productos_detalle.html
    |   |       productos_listado.html
    |   |       signup.html
    |   |       usuarios_listado.html
    |   |       
    |   \---__pycache__
    |           
    \---ecommerce
        |   asgi.py
        |   settings.py
        |   urls.py
        |   wsgi.py
        |   __init__.py
        |   
        \---__pycache__
```

#
## Tecnologías utilizadas
- [Bootstrap 5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/) 
- [Python 3.11](https://www.python.org/downloads/)
- [Django 4.2](https://docs.djangoproject.com/) 
- [PostgreSQL 16](https://www.postgresql.org/download/)

#
## Instalación

1. Clonar el repositorio desde git bash

    >```bash
    >git clone https://github.com/proyectodjangocacgrupo6/proyectodjango.git
    >```

2. Acceder a la carpeta del proyecto

    >```bash
    >cd ruta/proyectodjango
    >```

3. Crear un entorno virtual

    >```bash
    >python -m venv "nombre_entorno_virtual" 
    >```

4. Activar el entorno virtual

    >*Linux / macOS*
    >
    >```bash
    >ruta_al_entorno_virtual/nombre_entorno_virtual/bin/activate
    >```
    >
    >*Windows*
    >
    >```bash
    >ruta_al_entorno_virtual\nombre_entorno_virtual\Scripts\activate
    >```

5. Instalar las dependencias

    >```bash
    >pip install -r requirements.txt
    >```

6. Crear la base de datos en PostgreSQL:

    1. Abre pgAdmin y haz clic derecho en “Databases”.
    2. Selecciona “Create” y luego “Database”.
    3. Ingresa el nombre de la base de datos y selecciona el propietario.

7. Crear el archivo '.env' en la carpeta 'proyectodjango' con los siguientes parámetros

    ```text
    DB_NAME= 'tienda'
    DB_USER= 'postgres'
    DB_PASSWORD= 'password'
    DB_HOST=127.0.0.1
    DB_PORT=5432
    ````

8. Crear las tablas de la base de datos

    >```bash
    >python manage.py migrate
    >````

9. Crear un usuario administrador

    >```bash
    >python manage.py createsuperuser
    >````

10. Ejecutar el servidor local

    >```bash
    >python manage.py runserver
    >````

11. Acceder a <http://localhost:8000/> en el navegador

