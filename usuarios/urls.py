from django.urls import path

# Importa a variável 'views' que contém as funções de visualização para cada rota
from . import views

urlpatterns = [
    # Rota para a página de login, que chama a função 'login' em views
    path('login/', views.login, name='login'),

    # Rota para a página de cadastro, que chama a função 'cadastro' em views
    path('cadastro/', views.cadastro, name='cadastro'),

    # Rota para validar o cadastro, que chama a função 'validar_cadastro' em views
    path('validar_cadastro/', views.validar_cadastro, name='validar_cadastro'),

    # Rota para validar o login, que chama a função 'validar_login' em views
    path('validar_login/', views.validar_login, name='validar_login'),

    # Rota para o logout, que chama a função 'sair' em views
    path('sair/', views.sair, name='sair'),
]
