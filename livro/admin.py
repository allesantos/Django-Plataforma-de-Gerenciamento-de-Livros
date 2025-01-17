from django.contrib import admin

# Importa os modelos Livros, Categoria e Emprestimo definidos no app livro
from . models import Livros, Categoria, Emprestimo

# Registra o modelo Categoria no Django Admin
admin.site.register(Categoria)

# Registra o modelo Livros no Django Admin
admin.site.register(Livros)

# Registra o modelo Emprestimo no Django Admin
admin.site.register(Emprestimo)
