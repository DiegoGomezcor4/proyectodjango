from django.contrib import admin
from .models import Producto, Categoria, Usuario, Pedido, DetallePedido

# Register your models here.
# Registro de modelos para usarlos en el Admin
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
