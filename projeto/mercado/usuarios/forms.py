from django import forms
from .models import Produtos
from django.contrib.auth.models import User

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'perecivel', 'preco', 'marca', 'imagem']
        
class CadastroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff' ]