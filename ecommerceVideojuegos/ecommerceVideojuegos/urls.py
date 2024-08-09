"""
URL configuration for ecommerceVideojuegos project.

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
from django.contrib import admin
from django.urls import path,include
from catalogo.views import ayuda,index,comprar,contacto,noticias
from django.conf.urls.static import static
from django.conf import settings
#from login.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('ayuda/',ayuda,name='ayuda'),
    path('comprar/',comprar,name='comprar'),
    path('noticias/',noticias,name='noticias'),
    path('contacto/',contacto,name="contacto"),
    path('login/',include('django.contrib.auth.urls')),
    path('',include('login.urls')),
    path('carrito/',include('carrito.urls')),
#si no poner users  o / y users o login.urls en vez de users
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)