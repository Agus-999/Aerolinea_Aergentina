from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Avion
from .forms import AvionForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_aviones(request):
    aviones = Avion.objects.all()
    return render(request, 'Aviones/lista.html', {'aviones': aviones})

@login_required
def crear_avion(request):
    if request.method == 'POST':
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avión creado correctamente.')
            return redirect('lista_aviones')
    else:
        form = AvionForm()
    return render(request, 'Aviones/formulario.html', {'form': form, 'accion': 'Crear'})

@login_required
def editar_avion(request, avion_id):
    avion = get_object_or_404(Avion, id=avion_id)
    if request.method == 'POST':
        form = AvionForm(request.POST, instance=avion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avión actualizado correctamente.')
            return redirect('lista_aviones')
    else:
        form = AvionForm(instance=avion)
    return render(request, 'Aviones/formulario.html', {'form': form, 'accion': 'Editar', 'avion': avion})

@login_required
def eliminar_avion(request, avion_id):
    avion = get_object_or_404(Avion, id=avion_id)
    if request.method == 'POST':
        avion.delete()
        messages.success(request, 'Avión eliminado correctamente.')
        return redirect('lista_aviones')
    return render(request, 'Aviones/eliminar.html', {'avion': avion})
