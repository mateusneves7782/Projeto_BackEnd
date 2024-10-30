from django import forms
from .models import Usuario  # Certifique-se de que você tem um modelo chamado Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'email', 'idade']  # Ajuste conforme seus campos
