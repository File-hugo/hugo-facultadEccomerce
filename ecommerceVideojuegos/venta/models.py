from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Producto

class Producto(models.Model):
    fecha=models.DateTimeField()
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
#usuario que es una foreign key donde al borrar un usuario se borre la venta
    producto=models.ManyToManyField(Producto)
    
    
    
   

   # def __str__(self):
   #     return f'Producto nombre: {self.titulo} - Precio: {self.precio}'
