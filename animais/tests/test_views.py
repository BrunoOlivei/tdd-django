from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome='Calopsita',
            predador=False,
            venenoso=False,
            domestico=True
        ) # Cria um animal com as caracteristicas passadas

    def test_index_view_retorna_caracteristicas_do_animal(self):
        """Teste que verifica se a index retorna as caracteristicas do animal pesquisado"""
        response = self.client.get('/', {'buscar': 'Calopsita'}) # Passa um dicionário com a chave 'caracteristicas' e o valor 'resultado' para a rota /
        caracteristica_animal_pesquisado = response.context['caracteristicas'] # Atribui o valor da chave 'caracteristicas' do contexto da resposta a uma variável
        self.assertEqual(caracteristica_animal_pesquisado[0].nome, 'Calopsita') # Verifica se o nome do animal pesquisado é igual a 'Calopsita'
