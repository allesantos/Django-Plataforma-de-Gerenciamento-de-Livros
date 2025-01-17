"""
Configurações do Django para o projeto biblioteca.

Gerado pelo comando 'django-admin startproject' utilizando Django 5.0.4.

Mais informações sobre este arquivo podem ser encontradas em:
https://docs.djangoproject.com/en/5.0/topics/settings/

Para a lista completa de configurações e seus valores, consulte:
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Importa módulos necessários para a configuração de caminhos e manipulação de diretórios
from pathlib import Path
import os

# Caminho base do projeto, que aponta para o diretório principal do projeto
BASE_DIR = Path(__file__).resolve().parent.parent


# Configurações iniciais de desenvolvimento - não adequadas para produção
# Consulte https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/ para mais detalhes

# ATENÇÃO: Mantenha a chave secreta em segurança em produção!
SECRET_KEY = 'django-insecure-jdohd!!ejm8=$&^3ikn%j!07030-^7n*kcpa2cb&eofk&hugye'

# ATENÇÃO: Não execute o Django com DEBUG ativado em produção!
DEBUG = True

# Define os hosts permitidos para o projeto, útil para a segurança em produção
ALLOWED_HOSTS = []


# Definição das aplicações instaladas no Django
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin do Django
    'django.contrib.auth',   # Sistema de autenticação
    'django.contrib.contenttypes',  # Gerenciamento de tipos de conteúdo
    'django.contrib.sessions',  # Gerenciamento de sessões
    'django.contrib.messages',  # Mensagens temporárias para o usuário
    'django.contrib.staticfiles',  # Gerenciamento de arquivos estáticos
    'livro',  # Aplicação relacionada ao gerenciamento de livros
    'usuarios',  # Aplicação de usuários
]

# Middleware responsável por interceptar as requisições HTTP e adicionar funcionalidades
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Middleware de segurança
    'django.contrib.sessions.middleware.SessionMiddleware',  # Gerenciamento de sessões
    'django.middleware.common.CommonMiddleware',  # Middleware para funcionalidades comuns
    'django.middleware.csrf.CsrfViewMiddleware',  # Proteção contra CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware de autenticação
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware de mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protege contra ataques de clickjacking
]

# Configuração das URLs raiz do projeto
ROOT_URLCONF = 'biblioteca.urls'

# Configuração dos templates no Django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Usando o backend de templates do Django
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Diretórios onde o Django buscará templates
        'APP_DIRS': True,  # Permite buscar templates dentro de cada aplicação
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Adiciona variáveis de depuração
                'django.template.context_processors.request',  # Adiciona a requisição ao contexto
                'django.contrib.auth.context_processors.auth',  # Adiciona o usuário autenticado ao contexto
                'django.contrib.messages.context_processors.messages',  # Adiciona mensagens de status ao contexto
            ],
            'libraries': {
                'filtros': 'livro.templatetags.filtros',  # Define bibliotecas customizadas para templates
            }
        },
    },
]

# Configuração do WSGI para o Django, utilizado na aplicação web
WSGI_APPLICATION = 'biblioteca.wsgi.application'


# Configuração do banco de dados
# Para mais detalhes sobre bancos de dados, veja https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Utiliza o banco de dados SQLite
        'NAME': BASE_DIR / 'db.sqlite3',  # Caminho para o arquivo de banco de dados
    }
}


# Validação de senhas do Django
# Consulte https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators para mais informações

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Valida se a senha não é muito parecida com o nome do usuário
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Valida o comprimento mínimo da senha
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Valida se a senha não é uma senha comum
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Valida se a senha não é apenas numérica
    },
]


# Internacionalização e localização
# Consulte https://docs.djangoproject.com/en/5.0/topics/i18n/ para mais detalhes

LANGUAGE_CODE = 'pt-BR'  # Define o idioma do projeto como português brasileiro

TIME_ZONE = 'America/Sao_Paulo'  # Define o fuso horário para São Paulo

USE_I18N = True  # Ativa a internacionalização

USE_TZ = True  # Ativa o uso de fuso horário


# Arquivos estáticos (CSS, JavaScript, Imagens)
# Consulte https://docs.djangoproject.com/en/5.0/howto/static-files/ para mais detalhes

STATIC_URL = '/static/'  # URL para acessar arquivos estáticos
STATICFILES_DIRS = [BASE_DIR / 'static']  # Caminho para os arquivos estáticos na pasta do projeto
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Diretório onde os arquivos estáticos serão coletados para produção

# Configuração de arquivos de mídia (como imagens enviadas pelos usuários)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Diretório para armazenar os arquivos de mídia
MEDIA_URL = '/media/'  # URL para acessar arquivos de mídia

# Tipo de campo primário padrão (campo auto-incremento para IDs)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Usado para criar chaves primárias grandes
