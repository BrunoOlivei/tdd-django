from django.shortcuts import render
from animais.models import Animal

def index(request):
    context = {'caracteristicas': Animal.objects.all()} # Cria um dicionário com a chave 'caracteristicas' e o valor None
    return render(request, 'index.html', context) # Retorna uma resposta vazia