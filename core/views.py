from django.shortcuts import render, redirect
from .forms import ContactForm, AltaUsuarioForm, loginForm
from django.contrib.auth import login, logout
from .models import Usuario
from django.urls import reverse


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


def signup(request):
    context = {}

    if request.method == "POST":
        alta_form = AltaUsuarioForm(data=request.POST)
        if alta_form.is_valid():
            nuevo_usuario = Usuario(
                nombre=alta_form.cleaned_data["nombre"],
                apellido=alta_form.cleaned_data["apellido"],
                email=alta_form.cleaned_data["email"],
                password=alta_form.cleaned_data["password"],
                ciudad=alta_form.cleaned_data["ciudad"],
            )
            nuevo_usuario.save()
            # messages.info(request, "alumno dado de alta correctamente")
            return redirect(reverse("home"))

    else:
        alta_form = AltaUsuarioForm()

    context["alta_form"] = AltaUsuarioForm()
    return render(request, "signup.html", context)


# Validacion del Login
def login_views(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = loginForm(request, data=request.POST)
            if form.is_valid():
                email = form.get_email()
                login(request, email)
                return redirect("home")
            else:
                return render(request, "login.html")
        else:
            return render(request, "login.html", {"form": loginForm})
    else:
        return redirect("home")


# validacion del logout
def logout_view(request):
    logout(request)
    return redirect("home")
