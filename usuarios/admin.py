from django.contrib import admin 

# Importa o modelo Usuario da aplicação 'usuarios'
from usuarios.models import Usuario

# Registra o modelo 'Usuario' no Django Admin
@admin.register(Usuario)
class usuarioAdmin(admin.ModelAdmin):
    # Define os campos que serão somente leitura no painel de administração
    readonly_fields = ('nome', 'email', 'senha')  
