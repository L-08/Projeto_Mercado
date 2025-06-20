from django import forms
from .models import Produtos

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'perecivel', 'preco', 'marca', 'imagem']
        