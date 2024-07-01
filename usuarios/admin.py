from django.contrib import admin
from usuarios.models import Usuario

@admin.register(Usuario)
class usuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'senha')