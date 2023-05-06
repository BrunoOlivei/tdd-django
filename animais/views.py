from django.shortcuts import render
from animais.models import Animal

def index(request):
    contexto = {'caracteristicas': None} # Cria um dicionário com a chave 'caracteristicas' e o valor None
    if 'buscar' in request.GET: # Verifica se a chave 'buscar' está no dicionário request.GET
        animais = Animal.objects.all() # Atribui todos os animais a uma variável
        animal_pesquisado = request.GET['buscar'] # Atribui o valor da chave 'buscar' do dicionário request.GET a uma variável
        caracteristicas = animais.filter(nome__icontains=animal_pesquisado) # Atribui a uma variável os animais que possuem o nome parecido com o animal pesquisado
        contexto = {'caracteristicas': caracteristicas} # Cria um dicionário com a chave 'caracteristicas' e o valor da variável caracteristicas
    return render(request, 'index.html', contexto) # Retorna uma resposta vazia