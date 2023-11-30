"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from core.views import (
    home,
    contact,
    product,
    productos_detalle,
    signup,
    login_views,
    logout_view,
    usuarios_listado,
    crear_producto,
    buscar_producto,
    
)
from core import views

from django.contrib.auth import views as auth_views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("contacto/", contact, name="contact"),
    path("productos/", product, name="product"),
    # url parametrizada:
    path(
        "productos/detalle/<str:nombre_producto>/",
        productos_detalle,
        name="productos_detalle",
    ),
    path("signup", signup, name="signup"),
    path("login/", login_views, name="login"),
    path("logout/", logout_view, name="logout"),
    path('usuarios/listado', usuarios_listado, name='usuarios_listado'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login_admin.html'), name='login_admin'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout_admin.html'), name='logout_admin'),
    
    path('productos/listado', views.ProductoListView.as_view(), name='productos_listado'),
    
    path('crear_producto/', crear_producto, name='crear_producto'),
    
    path('buscar_producto/', buscar_producto, name='buscar_producto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
