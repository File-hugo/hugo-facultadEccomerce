# Generated by Django 5.0.3 on 2024-07-30 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=50, null=True)),
                ('precio', models.IntegerField(default=0, null=True)),
                ('fecha_lanzamiento', models.DateTimeField()),
                ('genero', models.CharField(max_length=50, null=True)),
                ('plataforma', models.CharField(max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(default='imagenes/juegoComprar1.png', upload_to='imagenes/')),
            ],
        ),
    ]
