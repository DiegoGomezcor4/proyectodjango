from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.
# Registro de modelos para usarlos en el Admin
admin.site.register(Producto)
admin.site.register(Categoria)
