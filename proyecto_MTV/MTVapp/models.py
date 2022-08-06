
from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre= models.CharField( max_length=40)
    apellido= models.CharField( max_length=40)
    edad= models.IntegerField()
    dni= models.IntegerField()
    domicilio= models.IntegerField()
    

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length =30)
    email = models.EmailField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField (max_length=30)
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    echa_entrega = models.DateField()
    entregado = models.BooleanField()
    
    


