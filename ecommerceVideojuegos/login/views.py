from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#si el usuario existe no es nulo. Si tiene user esta acreditado. Si hay error o no esta no lo esta.
# request post toma los name del login.html
#from django.http import HttpResponse

# request post toma los name del login.html
def login_usuario(request):
    #si el metodo de request:
    if (request.method=="POST"):
        usuario=request.POST['usuario']
        contraseña=request.POST['contraseña']
        user=authenticate(request,username=usuario,password=contraseña)
        if user is not None:
            print("exito")
            login(request,user)
            return redirect("videojuegos")#o comprar
        else:
            messages.success(request,"Hubo inconvenientes, reintenta")
            return redirect("login")
    return render(request, 'login.html')
    #Si no es post renderiza request

def logout_usuario(request):
    logout(request)#solo esto porque ya tengo el usuario definidio
    return redirect('videojuegos')