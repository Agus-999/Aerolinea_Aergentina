👤 Etapa 3: Registro y Login con roles personalizados
🧱 Objetivo
Implementamos un sistema de autenticación personalizado en Django, con soporte para roles (cliente y admin) mediante un modelo de usuario propio.
Además, personalizamos las vistas de login, logout y registro, y modificamos la interfaz para que muestre las opciones correspondientes según si el usuario ha iniciado sesión o no.

⚙️ 1. Configuración del modelo de usuario personalizado
📄 Archivo: home/models.py

Creamos un modelo Usuario heredando de AbstractBaseUser y usando un CustomUserManager para manejar la creación de usuarios y superusuarios:

python
Copiar código
class Usuario(AbstractBaseUser):
    ...
    rol = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('cliente', 'Cliente')], default='cliente')
🔑 El campo rol se asigna automáticamente:

'cliente' cuando el usuario se registra desde la web.

'admin' cuando se crea un superusuario usando el comando createsuperuser.

🧠 Luego en settings.py:

python
Copiar código
AUTH_USER_MODEL = 'home.Usuario'
✍️ 2. Formulario de registro personalizado
📄 Archivo: home/forms.py

Creamos un formulario RegistroForm basado en UserCreationForm que fuerza el rol 'cliente' al guardarlo:

python
Copiar código
def save(self, commit=True):
    user = super().save(commit=False)
    user.rol = 'cliente'
    ...
🔐 3. Vistas de autenticación
📄 Archivo: home/views.py

Implementamos las vistas para login, registro y logout usando AuthenticationForm y nuestros propios formularios:

login_view: inicia sesión y redirige al inicio.

register_view: registra usuarios con rol 'cliente'.

logout_view: cierra sesión.

Además, la vista inicio muestra el nombre de usuario y su rol si está autenticado.

🌐 4. Rutas configuradas
📄 Archivo: home/urls.py

python
Copiar código
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
📄 En aerolinea_voladora/urls.py incluimos estas rutas:

python
Copiar código
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
🖼️ 5. Plantillas HTML dinámicas
📄 base.html

html
Copiar código
<nav>
  <ul>
    <li><a href="{% url 'inicio' %}">Inicio</a></li>
    {% if user.is_authenticated %}
        <li><a href="{% url 'logout' %}">Cerrar sesión</a></li>
    {% else %}
        <li><a href="{% url 'login' %}">Iniciar sesión</a></li>
        <li><a href="{% url 'register' %}">Registrarse</a></li>
    {% endif %}
  </ul>
</nav>
📄 inicio.html

django
Copiar código
{% extends 'base.html' %}

{% block content %}
  {% if user.is_authenticated %}
    <h1>Bienvenido {{ user.username }}</h1>
    <p>Rol: {{ user.rol }}</p>
  {% else %}
    <p>Bienvenido visitante, por favor inicia sesión.</p>
  {% endif %}
{% endblock %}
✅ 6. Verificación
Creamos un superusuario:

bash
Copiar código
python manage.py createsuperuser
Verificamos que tenga rol admin.

Registramos un nuevo usuario desde la web:
✅ El rol asignado automáticamente es cliente.

Al iniciar sesión, las opciones del menú cambian según el estado.

🗂️ Estructura actual del proyecto
bash
Copiar código
aerolinea_voladora/
├── aerolinea_voladora/
│   └── settings.py
│   └── urls.py
├── home/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── inicio.html
│   │   └── assets/
│   │       ├── login.html
│   │       └── register.html
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── venv/
✍️ Autor
Agustín Alejandro Fasano