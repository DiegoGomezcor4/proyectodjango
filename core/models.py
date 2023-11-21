from django.db import models
from django.forms import ValidationError

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    apellido = models.CharField(max_length=30, verbose_name='Apellido')
    email = models.EmailField(max_length=150, verbose_name='Email')
    password = models.CharField(verbose_name='password')
    ciudad = models.CharField(max_length=150, verbose_name='ciudad')
    
    def __str__(self):
        return f"{self.nombre}"
    
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='categoria')
    
    def __str__(self):
        return f"{self.nombre}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    descripcion = models.CharField(max_length=150, verbose_name='descripcion')
    imagen = models.BinaryField(verbose_name='imagen')
    Stock = models.IntegerField(verbose_name='stock')
    precio = models.FloatField(verbose_name='precio')
    categoria = models.ManyToManyField(Categoria) # relacion muchos a muchos / producto -> categoria
    
    def __str__(self):
        return f"{self.nombre}"
    
 
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) # relacion uno a muchos / usuario->pedidos
    fecha_operacion = models.DateField()    


class DetallePedido(models.Model): # relacion muchos a uno / DetallePedido -> Pedido
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()