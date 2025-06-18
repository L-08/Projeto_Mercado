from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from usuarios.models import Produtos
from usuarios.forms import ProdutoForms


# Create your views here.
def tela_principal(request):
    contexto = {
        'produtos': Produtos.objects.all()
        
        
    }
    return render(request, 'produtos/tela_produtos.html', contexto)




