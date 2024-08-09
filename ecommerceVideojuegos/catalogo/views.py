import datetime
from django.shortcuts import render
#from django.http import HttpResponse
from .models import Producto
from catalogo.models import Producto
from .views import render

def productos(request):
    productos = Producto.objects.all()
    hoy = datetime.datetime.now()
    juegos = [
        'FallOut 64', 'Red Dead Redemption 2', 'Stalker', 'Far Cry',
        'Assasins Creed', 'FIFA 2024', 'Crysis', 'League of Legends',
        'F1 Manager 2024', 'Bo Path of the Teal Lotus'
    ]
    return render(request, 'index.html', {'fecha': hoy, 'productos': productos, 'juegos': juegos})

def ayuda(request):
    return render(request, 'ayuda.html')

def noticias(request):
    return render(request, 'noticias.html')

def comprar(request):
    hoy = datetime.datetime.now()
    productos = Producto.objects.all()
    juegos = [
        'FallOut 64', 'Red Dead Redemption 2', 'Stalker', 'Far Cry',
        'Assasins Creed', 'FIFA 2024', 'Crysis', 'League of Legends',
        'F1 Manager 2024', 'Bo Path of the Teal Lotus'
    ]
    return render(request, 'comprar.html', {'fecha': hoy, 'productos': productos, 'juegos': juegos})

def contacto(request):
    return render(request, 'contacto.html')

def resultado(request):
    return render(request, 'formularioEnviado.html')

def index(request):
    juegos = Producto.objects.all()
    return render(request, 'index.html', {'juegos': juegos})