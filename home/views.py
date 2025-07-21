from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm, EmpleadoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

# Vista de la página de inicio
def inicio(request):
    if request.user.is_authenticated:
        username = request.user.username
        rol = request.user.rol
    else:
        username = None
        rol = None
    return render(request, 'inicio.html', {'username': username, 'rol': rol})

# Vista de login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente.')
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'assets/login.html', {'form': form})

# Vista de registro
def register_view(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Te has registrado exitosamente. Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Error en el formulario de registro.')
    else:
        form = RegistroForm()
    return render(request, 'assets/register.html', {'form': form})

# Vista de logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('inicio')

# =========================
# CRUD EMPLEADOS
# =========================

@login_required
def lista_empleados(request):
    if request.user.rol != 'admin':
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('inicio')

    empleados = Usuario.objects.filter(rol='empleado')
    return render(request, 'assets/empleados/lista.html', {'empleados': empleados})

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
    return render(request, 'assets/empleados/formulario.html', {'form': form, 'accion': 'Crear'})

@login_required
def editar_empleado(request, empleado_id):
    if request.user.rol != 'admin':
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('inicio')

    empleado = get_object_or_404(Usuario, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado correctamente.')
            return redirect('assets/empleados/lista')
        else:
            messages.error(request, 'Error al actualizar el empleado.')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'assets/empleados/formulario.html', {'form': form, 'accion': 'Editar', 'empleado': empleado})

@login_required
def eliminar_empleado(request, empleado_id):
    if request.user.rol != 'admin':
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('inicio')

    empleado = get_object_or_404(Usuario, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        messages.success(request, 'Empleado eliminado correctamente.')
        return redirect('lista_empleados')
    return render(request, 'assets/empleados/eliminar.html', {'empleado': empleado})

# =========================
# CRUD CLIENTES
# =========================

from django.contrib.auth.decorators import user_passes_test

@login_required
@user_passes_test(lambda user: user.is_authenticated and user.rol == 'admin')
def lista_clientes(request):
    clientes = Usuario.objects.filter(rol='cliente')
    return render(request, 'assets/clientes/lista.html', {'clientes': clientes})

@login_required
@user_passes_test(lambda user: user.is_authenticated and user.rol == 'admin')
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Usuario, id=cliente_id, rol='cliente')
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado correctamente.')
            return redirect('lista_clientes')
        else:
            messages.error(request, 'Error al actualizar el cliente.')
    else:
        form = RegistroForm(instance=cliente)
    return render(request, 'assets/clientes/formulario.html', {'form': form})

@login_required
@user_passes_test(lambda user: user.is_authenticated and user.rol == 'admin')
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Usuario, id=cliente_id, rol='cliente')
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado correctamente.')
        return redirect('lista_clientes')
    return render(request, 'assets/clientes/eliminar.html', {'cliente': cliente})
