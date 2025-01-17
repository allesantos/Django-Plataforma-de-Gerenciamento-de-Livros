from django.contrib import admin  
from django.urls import path, include  # Funções para definir as rotas das URLs
from django.conf import settings  # Configurações do projeto, como caminhos para arquivos estáticos
from django.conf.urls.static import static  # Função para servir arquivos estáticos durante o desenvolvimento
from livro import views  # Views da aplicação 'livro' para exibir as páginas

# Definição das URLs do projeto
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para acessar o painel de administração do Django
    path('', views.home, name='home'),  # Rota para a página inicial do projeto, mapeada para a view 'home'
    path('livro/', include('livro.urls')),  # Inclui as URLs específicas da aplicação 'livro'
    path('auth/', include('usuarios.urls'))  # Inclui as URLs da aplicação 'usuarios', responsável por autenticação
]

# Serve arquivos de mídia (como imagens enviadas pelos usuários) durante o desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Adiciona o caminho para arquivos de mídia
