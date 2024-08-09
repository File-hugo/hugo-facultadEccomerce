from django.contrib import admin
from catalogo.models import Producto,Proveedor
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=("titulo","descripcion","precio","fecha_lanzamiento",
        "genero","plataforma", "activo","imagen")
    list_filter=["activo"]
    search_fields=["titulo"]

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Proveedor)
