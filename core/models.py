from django.db import models
from django.forms import ValidationError

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    apellido = models.CharField(max_length=30, verbose_name='Apellido')
    email = models.EmailField(max_length=150, verbose_name='Email')
    password = models.CharField(verbose_name='password')
    ciudad = models.CharField(max_length=150, verbose_name='ciudad')
    
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='categoria')
    
    
class Producto(models.Model):
    imagen = models.BinaryField(verbose_name='imagen')
    descuento = models.FloatField(verbose_name='descuento')
    precio = models.FloatField(verbose_name='precio')
    descripcion = models.CharField(max_length=150, verbose_name='descripcion')
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    categoria = models.ManyToManyField(Categoria) # relacion muchos a muchos / producto -> categoria
    
 
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) # relacion uno a muchos / usuario->pedidos
    fecha_operacion = models.DateField()    


class DetallePedido(models.Model): # relacion muchos a uno / DetallePedido -> Pedido
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()