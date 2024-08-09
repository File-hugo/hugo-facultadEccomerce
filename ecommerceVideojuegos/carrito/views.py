from django.shortcuts import render, redirect
from .Carro import Carro
from catalogo.models import Producto

# Create your views here.

def carro_resumen(request):
    carro = Carro(request)
    request.session['cantidad']=carro.__len__()
    return render(request, 'carro_resumen.html', {'carro':carro,'cantidad':carro.__len__()})

def carro_agregar(request, producto_id):
    # obtener el carro de la sesion
    carro = Carro(request)

    # buscamos el libro en nuestra BD por id
    producto = Producto.objects.get(id=producto_id)
    #libro = Libro.objects.get(id=id)

    carro.agregar(producto)
    request.session['cantidad']=carro.__len__()
    #para actualizar la cantidad
    #print(carro)
    #id=5
    print(f"id recibido{producto_id}")
    #return redirect('carro_resumen')
    return redirect('comprar')

def carro_limpiar(request):
    carro=Carro(request)
    carro.limpiar()
    #request.session['cantidad']=carro.__len__()
    return redirect('comprar')

def carro_borrar(request,producto_id):
    #obtengo el carro de la sesion
    carro=Carro(request)
    carro.borrar(producto_id)
    request.session['cantidad']=carro.__len__()
    return redirect('carro_resumen')

    
def carro_actualizar(request):
    pass
