🏠 Etapa 2: Creación de la app home y estructura base de la web

🔧 Creación de la app principal (home)  
Creamos una nueva app dentro del proyecto Django para manejar la parte principal del sitio:

    python manage.py startapp home

🧠 Registro de la app en Django  
Agregamos `'home'` a la lista de `INSTALLED_APPS` en el archivo `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'home',
]
🌐 Configuración de rutas
En aerolinea_voladora/urls.py, incluimos las URLs de la app home:

python
Copiar código
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
Creamos el archivo home/urls.py con la ruta base para la página de inicio:

python
Copiar código
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
📄 Creación de vistas y plantillas

📌 En home/views.py, definimos la vista para la página inicial:

python
Copiar código
from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')
📂 Estructura de carpetas de templates:

arduino
Copiar código
home/
└── templates/
    ├── base.html
    └── inicio.html
📄 En base.html, definimos la estructura principal del sitio:

html
Copiar código
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Aerolínea Argentina{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
📄 En inicio.html, extendemos de la base y colocamos contenido inicial:

html
Copiar código
{% extends 'base.html' %}

{% block title %}Inicio{% endblock %}

{% block content %}
    <h1>Bienvenido a Aerolínea Argentina</h1>
    <p>Página de inicio sin estilos.</p>
{% endblock %}
✅ Verificación del funcionamiento
Ejecutamos el servidor y comprobamos que se visualiza la página de inicio correctamente:

nginx
Copiar código
python manage.py runserver
🗂️ Estructura actual del proyecto

markdown
Copiar código
aerolinea_voladora/
├── aerolinea_voladora/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   └── inicio.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── aerolineas_voladoras
├── manage.py
├── requirements.txt
└── venv/
✍️ Autor

Agustín Alejandro Fasano