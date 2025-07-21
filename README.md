**✈️ Etapa 4/Aviones: Gestión de Flota de Aviones**

**🧱 Objetivo**
En esta etapa desarrollamos un sistema CRUD completo para gestionar los aviones de la aerolínea. Los empleados con permisos pueden crear, ver, editar y eliminar registros de aviones, incluyendo detalles como modelo, capacidad, filas y columnas de asientos. Todo esto se integra dentro de la plataforma protegida por autenticación.

**⚙️ 1. Modelo de Avión**
📄 Archivo: gestion/models.py

Creamos un modelo Avion con los siguientes campos:

python
Copiar
Editar
class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    filas = models.PositiveIntegerField()
    columnas = models.PositiveIntegerField()
👉 Estos campos permiten representar la distribución de asientos de cada avión de forma estructurada.

**✍️ 2. Formulario para Avión**
📄 Archivo: gestion/forms.py

Creamos un formulario AvionForm para manejar la creación y edición de aviones de forma sencilla:

python
Copiar
Editar
class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['modelo', 'capacidad', 'filas', 'columnas']
**🔧 3. Vistas de Aviones**
📄 Archivo: gestion/views.py

Se crearon las vistas protegidas para realizar operaciones CRUD sobre los aviones:

lista_aviones: Muestra una tabla con todos los aviones.

crear_avion: Permite agregar un nuevo avión.

editar_avion: Modifica los datos de un avión existente.

eliminar_avion: Elimina un avión de la base de datos.

Todas las vistas requieren que el usuario esté autenticado y tenga el rol adecuado.

**🌐 4. Rutas configuradas**
📄 Archivo: gestion/urls.py

python
Copiar
Editar
urlpatterns = [
    path('aviones/', views.lista_aviones, name='lista_aviones'),
    path('aviones/nuevo/', views.crear_avion, name='crear_avion'),
    path('aviones/<int:avion_id>/editar/', views.editar_avion, name='editar_avion'),
    path('aviones/<int:avion_id>/eliminar/', views.eliminar_avion, name='eliminar_avion'),
]
📄 En aerolinea/urls.py principal se incluyó esta app:

python
Copiar
Editar
path('gestion/', include('gestion.urls')),
**🖼️ 5. Plantillas HTML**
📄 Archivo: Aviones/lista.html

Se muestra la lista de aviones en una tabla:

html
Copiar
Editar
<table border="1">
  <tr>
    <th>Modelo</th>
    <th>Capacidad</th>
    <th>Filas</th>
    <th>Columnas</th>
    <th>Acciones</th>
  </tr>
  {% for avion in aviones %}
    <tr>
      <td>{{ avion.modelo }}</td>
      <td>{{ avion.capacidad }}</td>
      <td>{{ avion.filas }}</td>
      <td>{{ avion.columnas }}</td>
      <td>
        <a href="{% url 'editar_avion' avion.id %}">Editar</a>
        <a href="{% url 'eliminar_avion' avion.id %}">Eliminar</a>
      </td>
    </tr>
  {% endfor %}
</table>
📄 Formulario: Aviones/formulario.html

Formulario para crear o editar un avión:

html
Copiar
Editar
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Guardar</button>
</form>
✅ 6. Migraciones y base de datos
Se realizaron correctamente las migraciones:

bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
El modelo Avion fue agregado sin errores y se puede interactuar con él desde el panel de Django o las vistas.

**🗂️ Estructura del proyecto**
bash
Copiar
Editar
aerolinea/
├── aerolinea/
│   ├── settings.py
│   ├── urls.py
├── gestion/
│   ├── templates/
│   │   └── Aviones/
│   │       ├── lista.html
│   │       ├── formulario.html
│   │       └── eliminar.html
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── home/
│   ├── models.py (Usuario personalizado)
│   └── views.py (Login/Logout)
└── manage.py
**✍️ Autor**
Agustín Alejandro Fasano