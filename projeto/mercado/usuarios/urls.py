from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path("vendedores/", views.tela_vendedores, name='vendedores'),
]