from django import forms


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
    )


class loginForm(forms.Form):
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
