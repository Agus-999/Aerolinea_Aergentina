from django.urls import path
from . import views

urlpatterns = [
    path('aviones/', views.lista_aviones, name='lista_aviones'),
    path('aviones/nuevo/', views.crear_avion, name='crear_avion'),
    path('aviones/editar/<int:avion_id>/', views.editar_avion, name='editar_avion'),
    path('aviones/eliminar/<int:avion_id>/', views.eliminar_avion, name='eliminar_avion'),
]
