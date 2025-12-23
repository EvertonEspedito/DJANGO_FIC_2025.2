from django.shortcuts import render
from .models import Pessoa, Descricao

# Create your views here.
def index(request): # Para index.html
    """Pagina inicial para Learning Log."""
    return render(request, 'index.html')

def sobre(request): # Para sobre.html
    """Pagina sobre o sistema SCP."""
    return render(request, 'sobre.html')

def pessoas(request): # Para pessoas.html
    """Pagina para gerenciar pessoas cadastradas."""
    pessoas = Pessoa.objects.order_by('date_added') # Ordena as pessoas pela data de adição
    context = {'pessoas': pessoas} # Dicionário de contexto para passar para o template
    return render(request, 'pessoas.html', context)

def pessoa(request, pessoa_id): # Para pessoa.html
    """Pagina para exibir detalhes de uma pessoa individual."""
    # Aqui você pode adicionar lógica para obter uma pessoa específica
    pessoa = Pessoa.objects.get(id=pessoa_id)
    context = {} # Dicionário de contexto para passar para o template
    return render(request, 'pessoa.html', context)