from django.db import models


class Disco(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.IntegerField()
    año = models.IntegerField()

    #def __str__(self):
       # return self.nombre
    
class Disco_comprado (models.Model):
    nombre = models.CharField(max_length=30)
    autor = models.IntegerField()
    fecha_de_compra = models.DateField()
    
class Disco_vendido (models.Model):
    nombre = models.CharField(max_length=30)
    autor = models.IntegerField()
    fecha_de_compra = models.DateField()

class Usuario_comprador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Usuario_vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
   









