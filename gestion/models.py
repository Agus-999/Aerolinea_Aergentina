from django.db import models

class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    filas = models.IntegerField(default=0)  # Valor predeterminado para filas
    columnas = models.IntegerField(default=0)  # Valor predeterminado para columnas

    def __str__(self):
        return self.modelo
