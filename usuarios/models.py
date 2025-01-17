from django.db import models

# Define o modelo 'Usuario' que representa um usuário no sistema
class Usuario(models.Model):
    # Campo 'nome' do usuário, do tipo CharField, com um limite máximo de 30 caracteres
    nome = models.CharField(max_length=30)
    
    # Campo 'email' do usuário, do tipo EmailField, utilizado para armazenar endereços de e-mail
    email = models.EmailField()

    # Campo 'senha' do usuário, do tipo CharField, com um limite máximo de 64 caracteres
    senha = models.CharField(max_length=64)

    # Define o método __str__ para representar o objeto de forma legível
    # Retorna o nome do usuário como representação em string do objeto
    def __str__(self) -> str:
        return self.nome



