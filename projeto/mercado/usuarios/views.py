from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForms
from usuarios.models import Produtos


# Create your views here.
def cadastro(request:HttpRequest):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        username = request.POST.get("username")
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Já existem um usruario com este nome!")
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse("usuario cadastrado com sucesso")
    

def login(request):
    if request.method == "GET":
        return render(request, "usuarios/login.html")
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse("autenticado")
        else:
            return HttpResponse("Usuario ou senha inválidos")
    

@login_required(login_url='/auth/login/')
def tela_vendedores(request:HttpRequest):
    if request.method == "POST":
        file = request.FILES.get('imagem')
        formulario = ProdutoForms(request.POST)
        if formulario.is_valid():
            formulario.save()

            return redirect('produtos:tela_produtos')
        
    contexto ={
        
        'form':ProdutoForms
    }

    
    return render(request, 'usuarios/tela_vendedores.html', contexto)


@login_required(login_url='/auth/login/')
def detalhes(request:HttpRequest):
    contexto = {
        'produtos':Produtos.objects.all()
    }
    return render(request, 'usuarios/detalhes.html', contexto)

@login_required(login_url='/auth/login/')
def tela_remover(request:HttpRequest, id):
    produto = get_object_or_404(Produtos,id=id)
    produto.delete()
    return render(request, 'usuarios/remover_produtos.html')


@login_required(login_url='/auth/login/')
def tela_editar(request:HttpRequest, id):
    produto = get_object_or_404(Produtos, id=id)
    if request.method == "POST":
        formulario = ProdutoForms(request.POST, instance=produto)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:detalhes')
    
    formulario = ProdutoForms(instance=produto)
    contexto = {
        'form': formulario
    }
    return render(request, 'usuarios/editar.html', contexto)