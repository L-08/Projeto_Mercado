from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def tela_principal(request):
    return render(request, 'tela_produtos.html')




