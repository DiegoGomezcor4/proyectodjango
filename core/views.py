from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def product(request):
    return render(request, "product.html")


# view parametrizada:
def productos_detalle(request, nombre_producto):
    nombre_prod = nombre_producto

    context = {
        "nombre": nombre_prod,
    }

    return render(request, "productos_detalle.html", context)


##contact form


def contact(request):
    # print('tipo de peticion: {}'.format(request.method))

    contact_form = ContactForm
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            first_name = request.POST.get("first_name", "")
            last_name = request.POST.get("last_name", "")
            contry = request.POST.get("contry", "")
            city = request.POST.get("city", "")
            email = request.POST.get("email", "")
            descripcion = request.POST.get("descripcion", "")

    return render(request, "contact.html", {"form": contact_form})
