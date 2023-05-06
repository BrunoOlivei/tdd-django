from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_retorna_caracteristicas_do_animal(self):
        """Teste que verifica se a index retorna as caracteristicas do animal pesquisado"""
        response = self.client.get('/', {'caracteristicas': 'resultado'}) # Passa um dicionário com a chave 'caracteristicas' e o valor 'resultado' para a rota /
        self.assertIs(type(response.context['caracteristicas']), QuerySet) # Verifica se o tipo do valor da chave 'caracteristicas' do contexto da resposta é QuerySet