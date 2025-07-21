👤 **Etapa 3/Empleados_y_Roles_Personalizados: Gestión de Empleados y Clientes con Roles Personalizados**

🧱 **Objetivo**  
En esta etapa, implementamos un sistema de autenticación y gestión de usuarios con roles personalizados, permitiendo la administración de empleados y clientes. Los administradores pueden gestionar la creación, edición y eliminación de empleados, mientras que los clientes tienen acceso restringido solo a su información. Además, personalizamos las vistas y plantillas para reflejar estas funcionalidades de manera dinámica.

⚙️ **1. Configuración del modelo de usuario personalizado**  
📄 **Archivo:** `home/models.py`

Creamos un modelo de usuario llamado `Usuario`, heredado de `AbstractBaseUser`, y usamos un `CustomUserManager` para manejar la creación de usuarios y superusuarios.  
Se añade un campo `rol` para diferenciar entre administradores y clientes.

```python
class Usuario(AbstractBaseUser):
    ...
    rol = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('empleado', 'Empleado'), ('cliente', 'Cliente')], default='cliente')
🔑 El campo rol se asigna automáticamente:

'cliente' cuando el usuario se registra desde la web.

'admin' cuando se crea un superusuario usando el comando createsuperuser.

En settings.py, se define el modelo de usuario personalizado:

python
Copiar código
AUTH_USER_MODEL = 'home.Usuario'
✍️ 2. Formularios personalizados
📄 Archivo: home/forms.py

Creamos un formulario EmpleadoForm basado en ModelForm para gestionar los empleados, con el campo rol predefinido como 'empleado' al crear un nuevo registro:

python
Copiar código
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.rol = 'empleado'
        if commit:
            user.save()
        return user
Formulario de registro: Utilizamos el formulario RegistroForm para registrar nuevos usuarios con el rol 'cliente' de manera predeterminada.

python
Copiar código
def save(self, commit=True):
    user = super().save(commit=False)
    user.rol = 'cliente'
    ...
🔐 3. Vistas de gestión de empleados y clientes
📄 Archivo: home/views.py

Implementamos las vistas para crear, editar y eliminar empleados y clientes, utilizando las funciones get_object_or_404, redirect y messages para mostrar mensajes de éxito o error. Las vistas permiten a los administradores gestionar empleados y clientes.

crear_empleado: Crea un nuevo empleado con rol empleado.

editar_empleado: Permite modificar los datos de un empleado existente.

eliminar_empleado: Elimina a un empleado del sistema.

lista_empleados: Muestra una lista de empleados.

lista_clientes: Muestra una lista de clientes.

python
Copiar código
@login_required
def crear_empleado(request):
    if request.user.rol != 'admin':
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('inicio')

    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.rol = 'empleado'
            empleado.save()
            messages.success(request, 'Empleado creado correctamente.')
            return redirect('lista_empleados')
        else:
            messages.error(request, 'Error al crear el empleado.')
    else:
        form = EmpleadoForm()
    return render(request, 'assets/empleados/crear.html', {'form': form})
🌐 4. Rutas configuradas
📄 Archivo: home/urls.py

Definimos las rutas para cada vista, incluyendo las vistas de empleados y clientes. Usamos la función include() para incluir las rutas de la app en el archivo principal urls.py.

python
Copiar código
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleados/<int:empleado_id>/editar/', views.editar_empleado, name='editar_empleado'),
    path('empleados/<int:empleado_id>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:cliente_id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
]
📄 En aerolinea_voladora/urls.py incluimos estas rutas:

python
Copiar código
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
🖼️ 5. Plantillas HTML dinámicas
📄 Archivo: base.html

En la plantilla base, se gestionan las opciones de menú dinámicas según el estado de autenticación del usuario.

html
Copiar código
<nav>
  <ul>
    <li><a href="{% url 'inicio' %}">Inicio</a></li>
    {% if user.is_authenticated %}
        <li><a href="{% url 'logout' %}">Cerrar sesión</a></li>
        <li><a href="{% url 'lista_empleados' %}">Empleados</a></li>
        <li><a href="{% url 'lista_clientes' %}">Clientes</a></li>
    {% else %}
        <li><a href="{% url 'login' %}">Iniciar sesión</a></li>
        <li><a href="{% url 'register' %}">Registrarse</a></li>
    {% endif %}
  </ul>
</nav>
📄 Archivo: inicio.html

La vista inicio.html muestra el nombre de usuario y su rol si está autenticado.

html
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
│   │       ├── empleados/
│   │       │   ├── crear.html
│   │       │   ├── editar.html
│   │       │   └── eliminar.html
│   │       └── clientes/
│   │           ├── crear.html
│   │           ├── editar.html
│   │           └── eliminar.html
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── venv/
✍️ Autor
Agustín Alejandro Fasano

css
Copiar código
