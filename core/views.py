from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ContactForm, AltaUsuarioForm, loginForm
from django.contrib.auth import login, logout
from .models import Usuario, Producto
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def product(request):
    return render(request, "product.html")


# view parametrizada:
def productos_detalle(request, nombre_producto):

    producto = get_object_or_404(Producto, nombre=nombre_producto)

    context = {
        "producto": producto,
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
                return render(request, "login.html", {form: "form"})
        else:
            return render(request, "login.html", {"form": loginForm})
    else:
        return redirect("home")


# validacion del logout
def logout_view(request):
    logout(request)
    return redirect("home")

# listado de usuarios requiere login:
@login_required  
def usuarios_listado(request):
   
    listado = Usuario.objects.all().order_by('apellido')
   
    context = {
       'fecha' : datetime.now(),
       'cant_usuarios' : 0,
       'listado_usuarios' : listado,
       'cant_usuarios' : len(listado)
    }
    return render(request, "usuarios_listado.html", context)




# vistas basadas en clases:

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    context_object_name = 'listado_productos'
    template_name = 'productos_listado.html'
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar la fecha actual al contexto
        context['fecha_actual'] = datetime.now()
        return context