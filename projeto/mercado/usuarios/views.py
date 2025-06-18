from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
            return HttpResponse("autenticado")
        else:
            return HttpResponse("Usuario ou senha inválidos")