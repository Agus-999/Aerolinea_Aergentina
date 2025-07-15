# 🛫 Etapa 1: Creación del proyecto y conexión con base de datos

1. ⚙️ Instalación de Django  
   Ya teníamos un entorno virtual creado previamente, así que instalamos Django directamente:

   ```bash
   pip install django
🧱 Creación del proyecto Django
Ejecutamos el siguiente comando para crear el proyecto base:

bash
Copiar código
django-admin startproject aerolinea
cd aerolinea
🗄️ Conexión con la base de datos
Usamos la base de datos SQLite que viene por defecto en Django. No fue necesario crear ni mover ninguna base manualmente. En el archivo settings.py, se mantiene la configuración por defecto:

python
Copiar código
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
✅ Migraciones iniciales
Ejecutamos las migraciones por defecto de Django para crear las tablas base:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
📁 Estructura actual del proyecto
markdown
Copiar código
aerolinea/
├── aerolinea/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
✍️ Autor
Agustín Alejandro Fasano