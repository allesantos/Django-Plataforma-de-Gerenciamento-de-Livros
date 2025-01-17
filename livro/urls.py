from django.urls import path
# Importa o módulo 'views' do app livro
from . import views

# Lista de URLs configuradas para o aplicativo
urlpatterns = [
    # Rota para a página inicial do sistema, associada à função 'home'
    path('home/', views.home, name='home'),

    # Rota para listar os livros cadastrados, associada à função 'livros'
    path('livros/', views.livros, name='livros'),

    # Rota para visualizar detalhes de um livro específico, identificando-o pelo ID
    path('ver_livro/<int:id>', views.ver_livros, name='ver_livros'),

    # Rota para exibir o formulário e cadastrar um novo livro
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),

    # Rota para excluir um livro específico, identificando-o pelo ID
    path('excluir_livro/<int:id>', views.excluir_livro, name='excluir_livro'),

    # Rota para exibir o formulário e cadastrar uma nova categoria de livros
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),

    # Rota para registrar um novo empréstimo de livro
    path('cadastrar_emprestimo/', views.cadastrar_emprestimo, name='cadastrar_emprestimo'),

    # Rota para processar a devolução de um livro emprestado
    path('devolver_livro/', views.devolver_livro, name='devolver_livro'),

    # Rota para atualizar os detalhes de um livro existente
    path('alterar_livro/', views.alterar_livro, name='alterar_livro'),

    # Rota para listar os empréstimos realizados
    path('emprestimos_realizados/', views.emprestimos_realizados, name='emprestimos_realizados'),

    # Rota para processar a avaliação de um empréstimo
    path('processa_avaliacao/', views.processa_avaliacao, name='processa_avaliacao')
]
