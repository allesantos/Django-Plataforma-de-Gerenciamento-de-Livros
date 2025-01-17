from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from usuarios.models import Usuario  # Modelo de usuários
from .models import Livros, Categoria, Emprestimo  # Modelos do aplicativo atual
from .forms import CadastroLivro, CategoriaLivro  # Formulários personalizados
from django.contrib import messages  # Para exibir mensagens de feedback ao usuário
from datetime import datetime  # Para manipular datas

# Função para a página inicial do sistema
def home(request):
    if request.session.get('usuario'):  # Verifica se o usuário está logado
        # Obtém o usuário logado pelo ID da sessão
        usuario = Usuario.objects.get(id=request.session['usuario'])

         # Filtra os livros associados ao usuário logado
        livros = Livros.objects.filter(usuario=usuario)
        total_livros = livros.count()

        # Filtra os empréstimos ativos do usuário logado
        emprestimos_usuario = Emprestimo.objects.filter(
            nome_emprestado=usuario,
            data_devolucao=None
        )

        # Livros disponíveis para empréstimo (livros com emprestado=False)
        livros_emprestar = Livros.objects.filter(usuario=usuario, emprestado=False)

        # Livros que já foram emprestados
        livros_emprestados = Livros.objects.filter(usuario=usuario, emprestado=True)

        # Configuração dos formulários
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)
        form_categoria = CategoriaLivro()

        # Lista de usuários disponíveis para empréstimos (excluindo o usuário logado)
        usuarios = Usuario.objects.exclude(id=usuario.id)

        # Renderiza o template com os dados necessários
        return render(
            request,
            'home.html',
            {
                'livros': livros,  # Todos os livros do usuário logado
                'usuario_logado': request.session.get('usuario'),
                'form': form,
                'status_categoria': request.GET.get('cadastro_categoria'),
                'form_categoria': form_categoria,
                'usuarios': usuarios,  # Usuários exceto o logado
                'livros_emprestar': livros_emprestar,  # Livros disponíveis para empréstimo
                'livros_emprestados': livros_emprestados,  # Livros que já foram emprestados
                'emprestimos': emprestimos_usuario,  # Empréstimos ativos para o modal de devolução
                'total_livros': total_livros,
            }
        )
    else:  # Caso o usuário não esteja logado
        # Exibe livros disponíveis sem login (limitado a 5)
        livros = Livros.objects.filter(emprestado=False)[:5] 
        return render(request, 'home.html', {
            'livros': livros,
            'usuario_logado': None,
            'form': None,
            'status_categoria': None,
            'form_categoria': None,
            'usuarios': None,
            'livros_emprestar': None,
            'total_livros': None,
            'livros_emprestados': None
        })

# Função para listar os livros cadastrados
def livros(request):
    if request.session.get('usuario'):  # Verifica se o usuário está logado
        # Obtém o usuário logado
        usuario = Usuario.objects.get(id=request.session['usuario'])

        # Obtém todos os livros do usuário logado
        livros = Livros.objects.filter(usuario=usuario)
        total_livros = livros.count()

        # Filtra os empréstimos ativos do usuário logado
        emprestimos_usuario = Emprestimo.objects.filter(
            nome_emprestado=usuario,
            data_devolucao=None
        )

        # Livros disponíveis para empréstimo (livros com emprestado=False)
        livros_emprestar = Livros.objects.filter(usuario=usuario, emprestado=False)

        # Livros que já foram emprestados
        livros_emprestados = Livros.objects.filter(usuario=usuario, emprestado=True)

        # Configuração dos formulários
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)
        form_categoria = CategoriaLivro()

        # Exclui o usuário logado da lista de usuários
        usuarios = Usuario.objects.exclude(id=usuario.id)

        # Renderiza o template 'livros.html' com os dados necessários
        return render(
            request,
            'livros.html',
            {
                'livros': livros,  
                'usuario_logado': request.session.get('usuario'),
                'usuario_nome': usuario.nome,  
                'form': form,
                'status_categoria': request.GET.get('cadastro_categoria'),
                'form_categoria': form_categoria,
                'usuarios': usuarios, 
                'livros_emprestar': livros_emprestar,  
                'livros_emprestados': livros_emprestados,  
                'total_livros': total_livros,
                'emprestimos': emprestimos_usuario,  
            }
        )
    else:
        return redirect('/auth/login/?status=2')  # Redireciona para login caso não esteja logado

# Função para exibir detalhes de um livro específico
def ver_livros(request, id):
    if request.session.get('usuario'): # Verifica se o usuário está logado
        livro = Livros.objects.get(id=id) # Obtém o livro pelo ID
        if request.session.get('usuario') == livro.usuario.id: # Verifica se o livro pertence ao usuário logado
            usuario = Usuario.objects.get(id=request.session['usuario'])

            # Filtra categorias associadas ao usuário logado
            categoria_livro = Categoria.objects.filter(usuario_id=request.session.get('usuario'))

            # Obtém os empréstimos ativos do usuário logado
            emprestimos_usuario = Emprestimo.objects.filter(
               nome_emprestado=usuario,
               data_devolucao=None
            )

            emprestimos = Emprestimo.objects.filter(
                livro = livro
            )

            # Configuração dos formulários
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

            form_categoria = CategoriaLivro()

            # Filtra todos os usuários registrados, exceto o usuário logado
            usuarios = Usuario.objects.exclude(id=usuario.id)

            # Obtém os livros do usuário logado
            livros = Livros.objects.filter(usuario_id=request.session.get('usuario'))

            # Livros disponíveis para empréstimo (livros com emprestado=False)
            livros_emprestar = Livros.objects.filter(usuario=usuario, emprestado=False)

            # Contagem total de livros do usuário
            total_livros = livros.count()

            # Renderiza o template 'ver_livro.html' com os dados necessários
            return render(
                request,
                'ver_livro.html',
                {
                    'livro': livro,
                    'categoria_livro': categoria_livro,
                    'emprestimos_ativo': emprestimos_usuario,  # Empréstimos ativos
                    'emprestimos': emprestimos,
                    'usuario_logado': request.session.get('usuario'),
                    'form': form,
                    'id_livro': id,
                    'form_categoria': form_categoria,
                    'usuarios': usuarios,  # Usuários exceto o logado
                    'livros_emprestar': livros_emprestar,  # Livros disponíveis para empréstimo
                    'total_livros': total_livros,
                    'template_name': 'ver_livro.html',  # Adiciona o nome do template
                }
            )
    else:
        return redirect('/auth/login/?status=2')

def cadastrar_livro(request):
    # Verifica se o método da requisição é POST
    if request.method == 'POST':
        # Cria um formulário com os dados enviados
        form = CadastroLivro(request.POST, request.FILES)
        # Obtém a imagem enviada pelo formulário
        imagem = request.FILES.get('img')
        # Verifica se o formulário é válido
        if form.is_valid():
            # Salva os dados do formulário no banco de dados
            form.save()
            # Redireciona para a página de listagem de livros
            return redirect('/livro/livros')
        else:
            # Retorna uma mensagem de erro em caso de dados inválidos
            return HttpResponse('Dados inválidos!')
        
def excluir_livro(request, id):
    # Deleta o livro com o ID especificado
    livro = Livros.objects.get(id = id).delete()
    # Redireciona para a página de listagem de livros
    return redirect('/livro/livros')

def cadastrar_categoria(request):
    # Cria um formulário para cadastro de categoria com os dados enviados
    form = CategoriaLivro(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    id_usuario = request.POST.get('usuario')
    # Verifica se o usuário autenticado corresponde ao usuário do formulário
    if int(id_usuario) == int(request.session.get('usuario')):
        # Cria e salva a nova categoria
        user = Usuario.objects.get(id = id_usuario)
        categoria = Categoria(nome = nome, descricao = descricao, usuario = user)
        categoria.save()
        # Redireciona indicando sucesso no cadastro
        return redirect('/livro/livros?cadastro_categoria=1')
    else:
        # Redireciona para logout em caso de usuário inválido
        return redirect('/auth/sair')

def cadastrar_emprestimo(request):
     # Verifica se o método da requisição é POST
     if request.method == 'POST':
         # Obtém os dados do formulário
         nome_emprestado = request.POST.get('nome_emprestado')
         nome_emprestado_anonimo = request.POST.get('nome_emprestado_anonimo')
         livro_emprestado = request.POST.get('livro_emprestado')

        # Cria o empréstimo com base nos dados fornecidos
         if nome_emprestado_anonimo:
            emprestimo = Emprestimo(nome_emprestado_anonimo = nome_emprestado_anonimo,
                                  livro_id = livro_emprestado)
         else:
            emprestimo = Emprestimo(nome_emprestado_id = nome_emprestado,
                                    livro_id = livro_emprestado)
         emprestimo.save()

        # Atualiza o status do livro para "emprestado"
         livro = Livros.objects.get(id=livro_emprestado)
         livro.emprestado = True
         livro.save()

        # Redireciona para a página de listagem de livros
         return redirect('/livro/livros')

def devolver_livro(request):
    # Verifica se o método da requisição é POST
    if request.method == "POST":
        # Obtém o ID do livro enviado no formulário
        id = request.POST.get('id_livro_devolver')

        # Valida se o ID foi enviado
        if not id:
            messages.error(request, "ID do livro não foi enviado.")
            return redirect('/livro/livros')

        # Busca o livro no banco de dados
        livro_devolver = get_object_or_404(Livros, id=id)

        # Tenta obter o empréstimo ativo associado ao livro
        try:
            emprestimo_devolver = Emprestimo.objects.get(
                livro=livro_devolver,
                data_devolucao=None
            )
        except Emprestimo.DoesNotExist:
            messages.error(request, "Nenhum empréstimo ativo foi encontrado para este livro.")
            return redirect('/livro/livros')

        # Verifica a permissão do usuário para devolver o livro
        usuario_logado_id = request.session.get('usuario')
        if emprestimo_devolver.nome_emprestado.id != usuario_logado_id:
            messages.error(request, "Você não tem permissão para devolver este livro.")
            return redirect('/livro/livros')

        # Atualiza o status do livro para "não emprestado"
        livro_devolver.emprestado = False
        livro_devolver.save()

        # Atualiza a data de devolução no empréstimo
        emprestimo_devolver.data_devolucao = datetime.now()
        emprestimo_devolver.save()

        # Mensagem de sucesso
        messages.success(request, "Livro devolvido com sucesso.")
        return redirect('/livro/livros')

    # Caso o método não seja POST
    messages.error(request, "Método não permitido.")
    return redirect('/livro/livros')

def alterar_livro(request):
    # Obtém os dados do formulário
    livro_id = request.POST.get('livro_id')
    nome_livro = request.POST.get('nome_livro')
    autor = request.POST.get('autor')
    co_autor = request.POST.get('co_autor')
    categoria_id = request.POST.get('categoria_id')
    categoria = Categoria.objects.get(id = categoria_id)
    
    # Atualiza os dados do livro caso o usuário autenticado seja o proprietário
    livro = Livros.objects.get(id = livro_id)
    if livro.usuario.id == request.session['usuario']:
        livro.nome = nome_livro
        livro.autor = autor
        livro.co_autor = co_autor
        livro.categoria = categoria
        livro.save()
        return redirect(f'/livro/ver_livro/{livro_id}')
    else:
        return redirect('/auth/sair')
    
def emprestimos_realizados(request):
    # Obtém o usuário autenticado
    usuario = Usuario.objects.get(id=request.session['usuario'])

    # Filtra empréstimos ativos onde o usuário logado é o destinatário
    emprestimos = Emprestimo.objects.filter(nome_emprestado=usuario, data_devolucao=None)

    # Lista de livros emprestados ao usuário logado
    livros_emprestados = [emprestimo.livro for emprestimo in emprestimos]

    # Filtra livros que estão disponíveis para empréstimo (não emprestados)
    livros_emprestar = Livros.objects.filter(usuario=usuario, emprestado=False)

    # Configuração dos formulários
    form = CadastroLivro()
    form.fields['usuario'].initial = request.session['usuario']
    form.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)
    form_categoria = CategoriaLivro()
    livros = Livros.objects.filter(usuario_id=request.session.get('usuario'))
    total_livros = livros.count()

    # Obtém todos os usuários para o dropdown de empréstimos registrados, exceto o usuário logado
    usuarios = Usuario.objects.exclude(id=usuario.id)

    # Renderiza a página com os dados necessários
    return render(
        request,
        'emprestimos_realizados.html',
        {
            'usuario_logado': request.session['usuario'],
            'emprestimos': emprestimos,  # Envia os empréstimos para o template
            'livros_emprestados': livros_emprestados,  # Livros para devolução
            'livros_emprestar': livros_emprestar,  # Livros disponíveis para empréstimo
            'usuarios': usuarios,  # Usuários para empréstimos registrados, excluindo o logado
            'form': form,
            'form_categoria': form_categoria,
            'total_livros': total_livros,
        }
    )
   
def processa_avaliacao(request):
    # Obtém os dados do formulário
    id_emprestimo = request.POST.get('id_emprestimo')
    opcoes = request.POST.get('opcoes')
    id_livro = request.POST.get('id_livro')
    id_livro_logado = request.session['usuario']

    # Verifica se o empréstimo pertence ao usuário autenticado
    emprestimo = Emprestimo.objects.get(id = id_emprestimo)
    if emprestimo.livro.usuario.id == request.session['usuario']:
        # Atualiza a avaliação do empréstimo
        emprestimo.avaliacao = opcoes
        emprestimo.save()
        return redirect(f'/livro/ver_livro/{id_livro}')
    else:
        return HttpResponse('Este empréstimo não é seu!')




    

    
       
