from django.db import models

class Producto(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=50, null=True)
    precio = models.IntegerField(default=0, null=True)
    fecha_lanzamiento = models.DateTimeField()
    genero = models.CharField(max_length=50, null=True)
    plataforma = models.CharField(max_length=50, null=True)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='imagenes/', default="imagenes/juegoComprar1.png")

    def __str__(self):
        return f'Producto nombre: {self.titulo} - Precio: {self.precio}'

class Proveedor(models.Model):
    pagina_web = models.CharField(max_length=30, null=True)
    nombre_empresa = models.CharField(max_length=30, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Nombre proveedor: {self.nombre_empresa}'

class Contacto(models.Model):
    nombre = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    mensaje = models.TextField(null=True)

    def __str__(self):
        return f'Nombre contacto: {self.nombre}'