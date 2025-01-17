# Importação do módulo template do Django para criar filtros personalizados para templates
from django import template
from datetime import datetime  # Importação do módulo datetime para trabalhar com datas e horas

# Registro da biblioteca de filtros personalizados
register = template.Library()

# Definindo um filtro personalizado chamado 'mostra_duracao' que pode ser usado nos templates
@register.filter
def mostra_duracao(value1, value2):
    # Verifica se ambas as variáveis de entrada são instâncias do tipo 'datetime'
    if all((isinstance(value1, datetime), isinstance(value2, datetime))):
        # Calcula a diferença em dias entre as duas datas
        dias = (value1 - value2).days
        texto = 'dias'  # Caso a diferença seja maior que 1, utiliza o plural 'dias'
        
        # Se a diferença for exatamente 1 dia, altera para 'dia' no singular
        if dias == 1:
            texto = 'dia'
        
        # Retorna a string formatada com a quantidade de dias e o texto apropriado
        return f"{dias} {texto}"
    
    # Caso as entradas não sejam datas ou o valor da diferença não seja válido, retorna mensagem padrão
    return 'Ainda não foi devolvido!'
