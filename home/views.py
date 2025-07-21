from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Vista de la página de inicio
def inicio(request):
    if request.user.is_authenticated:
        username = request.user.username
        rol = request.user.rol  # Usamos el campo rol del modelo personalizado
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
