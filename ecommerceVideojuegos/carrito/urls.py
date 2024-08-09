"""
URL configuration for prueba5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import carro_resumen, carro_agregar, carro_borrar,carro_limpiar,carro_actualizar

urlpatterns = [    
    path('', carro_resumen, name='carro_resumen'),
    path('agregar/<producto_id>', carro_agregar, name='carro_agregar'),
    path('borrar/<producto_id>', carro_borrar, name='carro_borrar'),
    path('actualizar/', carro_actualizar, name='carro_actualizar'),
    path('limpiar/', carro_limpiar, name='carro_limpiar'),

]
