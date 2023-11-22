from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ValidationError

from core.models import Producto


class ContactForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "First name",
                "aria-label": "First name",
            }
        ),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Last name",
                "aria-label": "Last name",
            }
        ),
    )
    contry = forms.CharField(
        required=True,
        max_length=15,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "style": "margin-top: 15px",
                "placeholder": "Contry",
                "aria-label": "Contry",
            }
        ),
    )
    city = forms.CharField(
        required=True,
        max_length=15,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "style": "margin-top: 15px",
                "placeholder": "City",
                "aria-label": "City",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "id": "exampleFormControlInput1",
                "name": "email",
                "placeholder": "name@example.com",
            }
        ),
    )
    descripcion = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "exampleFormControlTextarea1",
                "placeholder": "Descripcion",
                "rows": "3",
            }
        ),
    )


class AltaUsuarioForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Nombre",
                "aria-label": "Nombre",
            }
        ),
    )
    apellido = forms.CharField(
        label="Apellido",
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Apellido",
                "aria-label": "Apellido",
            }
        ),
    )

    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "id": "exampleFormControlInput1",
                "name": "email",
                "placeholder": "nombre@ejemplo.com",
            }
        ),
    )
    password = forms.CharField(
        label="contraseña",
        required=True,
        max_length=15,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "style": "margin-top: 15px",
                "placeholder": "Password",
                "aria-label": "Password",
            }
        ),
    )

    ciudad = forms.CharField(
        label="ciudad",
        required=True,
        max_length=15,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "style": "margin-top: 15px",
                "placeholder": "Ciudad",
                "aria-label": "Ciudad",
            }
        ),
        error_messages={
            'invalid': 'La ciudad no es válida. Por favor, ingrese una ciudad válida.'
        }
    )

    
    # Validación en el backend:
    def clean(self):
        cleaned_data = super().clean()
        ciudad = cleaned_data.get('ciudad')
        # Ejemplo de validación de la ciudad (puedes personalizar esto según tus necesidades)
        if ciudad.lower() not in ['buenos aires', 'cordoba', 'rosario']:
            raise ValidationError({'ciudad': self.fields['ciudad'].error_messages['invalid']})

# Formulario basado en clases (AuthenticationForm hereda de forms.Form) -> class AuthenticationForm(forms.Form)
class loginForm(AuthenticationForm):
    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "id": "exampleFormControlInput1",
                "name": "email",
                "placeholder": "nombre@ejemplo.com",
            }
        ),
    )
    password = forms.CharField(
        label="contraseña",
        required=True,
        max_length=15,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "style": "margin-top: 15px",
                "placeholder": "Password",
                "aria-label": "Password",
            }
        ),
    )

# formulario asociado a un modelo
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'Stock', 'precio', 'categoria']

    imagen = forms.ImageField(required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Procesa el campo de imagen si se proporciona
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            instance.imagen = imagen.read()  # Guarda los bytes de la imagen en el campo de la base de datos

        if commit:
            instance.save()

        return instance