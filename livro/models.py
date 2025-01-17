# Importa o módulo de modelos do Django para criar tabelas no banco de dados
from django.db import models
# Importa a classe date para manipulação de datas
from datetime import date
# Importa o modelo de usuário personalizado
from usuarios.models import Usuario
# Importa o módulo datetime para manipulação de data e hora
import datetime

# Modelo para representar a categoria de livros
class Categoria(models.Model):
    # Campo para o nome da categoria (máximo 30 caracteres)
    nome = models.CharField(max_length=30)
    # Campo para descrição da categoria, exibido como "Descrição" no admin
    descricao = models.TextField(verbose_name="Descrição")
    # Relacionamento com o modelo de usuário, onde o usuário não é excluído mesmo que a categoria seja apagada
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    # Representação textual da categoria (exibida no admin ou em consultas)
    def __str__(self) -> str:
        return self.nome

# Modelo para representar livros
class Livros(models.Model):
    # Campo para imagem da capa do livro (opcional)
    img = models.ImageField(
        upload_to='capa_livro', 
        null=True, 
        blank=True, 
        verbose_name="Capa do Livro"
    )
    # Campo para o nome do livro (máximo 100 caracteres)
    nome = models.CharField(max_length=100)
    # Campo para o nome do autor (máximo 30 caracteres)
    autor = models.CharField(max_length=30)
    # Campo para o nome do coautor, opcional (máximo 30 caracteres)
    co_autor = models.CharField(
        max_length=30, 
        blank=True, 
        verbose_name="Coautor"
    )
    # Data de cadastro do livro, preenchida automaticamente com a data atual
    data_cadastro = models.DateField(
        default=date.today, 
        verbose_name="Data do Cadastro"
    )
    # Indica se o livro está emprestado (valor padrão: False)
    emprestado = models.BooleanField(default=False)
    # Relacionamento com a categoria do livro
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    # Relacionamento com o usuário responsável pelo livro
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    # Classe Meta para definir opções adicionais do modelo
    class Meta:
        # Nome singular usado no admin
        verbose_name = 'Livro'

    # Representação textual do livro (exibida no admin ou em consultas)
    def __str__(self):
        return self.nome

# Modelo para representar empréstimos de livros
class Emprestimo(models.Model):
    # Opções de avaliação para o empréstimo
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    # Relacionamento opcional com o usuário que realizou o empréstimo
    nome_emprestado = models.ForeignKey(
        Usuario, 
        on_delete=models.DO_NOTHING, 
        blank=True, 
        null=True
    )
    # Nome do usuário anônimo que realizou o empréstimo (opcional)
    nome_emprestado_anonimo = models.CharField(
        max_length=30, 
        blank=True, 
        null=True
    )
    # Data e hora do empréstimo, preenchida automaticamente
    data_emprestimo = models.DateTimeField(
        default=datetime.datetime.now()
    )
    # Data e hora da devolução (opcional)
    data_devolucao = models.DateTimeField(
        blank=True, 
        null=True
    )
    # Relacionamento com o livro emprestado
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    # Avaliação do empréstimo, escolhida entre as opções disponíveis (opcional)
    avaliacao = models.CharField(
        max_length=1, 
        choices=choices, 
        blank=True, 
        null=True
    )

    # Representação textual do empréstimo (exibida no admin ou em consultas)
    def __str__(self):
        return f'{self.nome_emprestado} | {self.livro}'
