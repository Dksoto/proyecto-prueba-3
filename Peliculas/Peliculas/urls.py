"""
URL configuration for Peliculas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view,name='login_view'), #inicio de sesion
    path('register/', register_view, name='register'), #registro
    path('dashboard/', dashboard, name='dashboard'), #index
    path('nueva_pelicula/', nueva_pelicula, name='nueva_pelicula'), #agregar
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'), #cerrar sesion
    path('borrar/<int:pelicula_id>/', borrar_pelicula, name='borrar_pelicula'), #borrar
    path('editar/<int:pelicula_id>/', editar_pelicula, name='editar_pelicula'), #editar
    path('admin/', admin1, name='admin'), #admin



]
