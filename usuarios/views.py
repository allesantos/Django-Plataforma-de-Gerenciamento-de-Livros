# Importa as funções necessárias para renderizar templates, manipular sessões e retornar respostas HTTP
from django.shortcuts import render
from django.http import HttpResponse
# Importa o modelo 'Usuario' para interagir com a base de dados
from .models import Usuario
from django.shortcuts import redirect
# Importa o módulo de hash SHA-256 para criptografar senhas
from hashlib import sha256

# Função de visualização para o login
def login(request):
    # Se o usuário já estiver logado (verificado através da sessão), redireciona para a página inicial
    if request.session.get('usuario'):
        return redirect('/livro/home/')
    
    # Obtém o status passado pela URL (se houver) para exibir mensagens de erro ou sucesso
    status = request.GET.get('status')
    # Renderiza a página de login com o status
    return render(request, 'login.html', {'status': status})

# Função de visualização para o cadastro
def cadastro(request):
    # Se o usuário já estiver logado, redireciona para a página inicial
    if request.session.get('usuario'):
        return redirect('/livro/home/')
    
    # Obtém o status passado pela URL (se houver) para exibir mensagens de erro ou sucesso
    status = request.GET.get('status')
    # Renderiza a página de cadastro com o status
    return render(request, 'cadastro.html', {'status': status})

# Função para validar o cadastro de um novo usuário
def validar_cadastro(request):
    # Obtém os dados enviados pelo formulário de cadastro
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    # Verifica se já existe um usuário com o mesmo email
    usuario = Usuario.objects.filter(email=email)

    # Verifica se o nome ou o email estão vazios, e redireciona com um status de erro
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    
    # Verifica se a senha tem pelo menos 8 caracteres, e redireciona com um status de erro
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    # Verifica se o usuário já existe no sistema (com o mesmo email), e redireciona com um status de erro
    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    # Tenta salvar o novo usuário, criptografando a senha antes de salvar no banco de dados
    try:
        senha = sha256(senha.encode()).hexdigest()  # Criptografa a senha usando SHA-256
        usuario = Usuario(nome=nome, senha=senha, email=email)
        usuario.save()  # Salva o novo usuário no banco de dados
        return redirect('/auth/cadastro/?status=4')  # Redireciona com status de sucesso
    
    # Caso ocorra um erro durante o cadastro, exibe um erro interno
    except:
        return redirect('/auth/cadastro/?status=5')

    # Código comentado: uma possível resposta para depuração
    # return HttpResponse(f"{nome} {senha} {email}")

# Função para validar o login do usuário
def validar_login(request):
    # Obtém os dados do formulário de login (email e senha)
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()  # Criptografa a senha antes de comparar

    # Verifica se existe um usuário com o email e a senha fornecidos
    usuario = Usuario.objects.filter(email=email).filter(senha=senha)

    # Se o usuário não for encontrado, redireciona para a página de login com um erro
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    
    # Se o usuário for encontrado, armazena o ID do usuário na sessão e redireciona para a página principal
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id  # Salva o ID do usuário na sessão
        return redirect(f'/livro/livros/?id_usuario={request.session["usuario"]}')
    
    # Código comentado: uma possível resposta para depuração
    return HttpResponse(f"{senha} {email}")

# Função para realizar o logout do usuário
def sair(request):
    # Limpa todos os dados da sessão, efetivamente desconectando o usuário
    request.session.flush()
    # Redireciona o usuário para a página de login
    return redirect('/auth/login/')
