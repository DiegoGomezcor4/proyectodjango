from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def product(request):
    return render(request, "product.html")

#view parametrizada:
def productos_detalle(request, nombre_producto):
    nombre_prod = nombre_producto

    context = {
        'nombre' : nombre_prod,
    }

    return render(request, "productos_detalle.html", context)
