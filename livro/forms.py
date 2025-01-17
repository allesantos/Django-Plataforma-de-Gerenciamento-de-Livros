# Importa a classe base para criação de formulários no Django
from django import forms
# Importa os modelos Livros e Emprestimo para serem utilizados nos formulários
from .models import Livros, Emprestimo

# Classe para o formulário de cadastro de livros
class CadastroLivro(forms.ModelForm):
    class Meta:
        # Define que o formulário está vinculado ao modelo Livros
        model = Livros
        # Inclui todos os campos do modelo Livros no formulário
        fields = "__all__"

    # Método especial para personalizar o formulário
    def __init__(self, *args, **kwargs):
        # Chama o método de inicialização da classe pai (ModelForm)
        super().__init__(*args, **kwargs)

        # Oculta o campo 'usuario' no formulário usando um widget HiddenInput
        self.fields['usuario'].widget = forms.HiddenInput()

        # Adiciona atributos como placeholder e classe CSS para estilizar os campos
        for field_name, field in self.fields.items():
            if field.widget.attrs is None:
                # Inicializa o atributo `attrs` caso ele seja None
                field.widget.attrs = {}
            # Adiciona um placeholder dinâmico baseado no label do campo
            field.widget.attrs['placeholder'] = f"Digite o {field.label.lower()}"
            # Adiciona a classe CSS 'form-control' para estilização padrão do Bootstrap
            field.widget.attrs['class'] = 'form-control'

        # Personaliza os campos que são do tipo CheckboxInput
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                # Adiciona a classe CSS 'custom-checkbox' para checkboxes personalizados
                field.widget.attrs['class'] = 'custom-checkbox'

# Classe para o formulário de cadastro de categorias
class CategoriaLivro(forms.Form):
    # Campo para o nome da categoria com validação de comprimento máximo e atributos personalizados
    nome = forms.CharField(
        max_length=30,  # Define o comprimento máximo de 30 caracteres
        widget=forms.TextInput(attrs={
            # Placeholder que orienta o usuário sobre o que preencher
            'placeholder': 'Digite o nome da categoria do livro',
            # Classe CSS 'form-control' para estilização
            'class': 'form-control'
        }),
        # Rótulo exibido no formulário
        label="Nome"
    )

    # Campo para a descrição da categoria, com limite de caracteres e área de texto personalizável
    descricao = forms.CharField(
        max_length=140,  # Define o comprimento máximo de 60 caracteres
        widget=forms.Textarea(attrs={
            # Placeholder para descrever a categoria
            'placeholder': 'Descreva a categoria (máximo 140 caracteres)',
            # Define o número de linhas exibidas no campo de texto
            'rows': 3,
            # Classe CSS 'form-control' para estilização
            'class': 'form-control'
        }),
        # Rótulo exibido no formulário
        label="Descrição:"
    )

    # Método especial para inicializar o formulário, podendo incluir personalizações futuras
    def __init__(self, *args, **kwargs):
        # Chama o método de inicialização da classe pai (Form)
        super().__init__(*args, **kwargs)
