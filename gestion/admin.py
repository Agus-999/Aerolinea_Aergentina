from django.contrib import admin
from .models import Avion

@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'capacidad', 'filas', 'columnas']
