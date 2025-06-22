from django.urls import path, include
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path("vendedores/", views.tela_vendedores, name='vendedores'),
    path('detalhes/', views.detalhes, name='detalhes'),
    path('remover/<int:id>', views.tela_remover, name='remover'),
    path('editar/<int:id>', views.tela_editar, name='editar')
]
