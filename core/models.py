from django.db import models
from django.forms import ValidationError

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    apellido = models.CharField(max_length=30, verbose_name='Apellido')
    email = models.EmailField(max_length=150, verbose_name='Email')
    password = models.CharField(verbose_name='password')
    ciudad = models.CharField(max_length=150, verbose_name='ciudad')