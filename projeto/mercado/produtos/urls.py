from django.urls import path
from . import views

app_name = 'produtos'
urlpatterns = [

    path("", views.tela_principal, name='principal'),

]