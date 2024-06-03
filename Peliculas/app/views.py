from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect , get_object_or_404
from .models import Pelicula #importar el modelo
from .forms import PeliculaForm #importar el formulario
from django.contrib.auth import logout #cerrar sesion


def dashboard(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'index.html', {'peliculas': peliculas})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(dashboard)  # Redirige a la página de inicio del usuario autenticado
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})





def nueva_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PeliculaForm()
    return render(request, 'nueva_pelicula.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login_view')  # redirige a la página de inicio de sesión




def borrar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    pelicula.delete()
    peliculas = Pelicula.objects.all()
    return render(request, 'index.html', {'peliculas': peliculas})

def editar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'editar_pelicula.html', {'form': form})







