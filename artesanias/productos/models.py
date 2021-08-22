from django.db import models

# Create your models here.


class Artesanias(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del producto")
    municipio =  models.CharField(max_length=100,verbose_name="Municipio de origen")
    costo = models.FloatField(verbose_name="Precio del producto")
    descripcion = models.TextField(verbose_name="Descripcion")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizado")

    class Meta:
        verbose_name = "Productos"
        verbose_name_plural = "Productos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre



#banners

class Banners(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizado")

    class Meta:
        verbose_name = "Banners"
        verbose_name_plural = "Banners"
        ordering = ["created"]

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    telefono = models.CharField(max_length=100, verbose_name="Telefono")
    email = models.EmailField(max_length=100, verbose_name="Correo")
    mensaje = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizado")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre


