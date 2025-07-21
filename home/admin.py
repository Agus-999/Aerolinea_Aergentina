from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Personalizamos UserAdmin para el modelo Usuario
class UsuarioAdmin(UserAdmin):
    model = Usuario
    # Definimos qué campos se deben mostrar en la lista de usuarios
    list_display = ('username', 'email', 'rol', 'is_active', 'is_staff')  # Usamos los campos existentes
    list_filter = ('rol', 'is_active', 'is_staff')  # Filtros disponibles en el admin
    search_fields = ('username', 'email')  # Búsqueda por nombre de usuario y correo electrónico
    ordering = ('username',)  # Ordenar por el nombre de usuario

    # Definimos los campos que se verán al agregar o editar un usuario
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Información de roles', {'fields': ('rol',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
        ('Información de roles', {'fields': ('rol',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

admin.site.register(Usuario, UsuarioAdmin)
