from django.test import TestCase,RequestFactory
from django.urls import reverse
from animais.views import index


class AnimaisURLsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory() # Cria uma instância de RequestFactory necessária utilizar métodos de request

    def test_rota_url_utiliza_view_index(self):
        """Teste se a home da aplicação utiliza a função index da view"""
        request = self.factory.get('/') # Cria um request do tipo GET para a rota /
        with self.assertTemplateUsed('index.html'): # Verifica se o template index.html é utilizado
            response = index(request) # Passa o request para a função index da view
            self.assertEqual(response.status_code, 200) # Verifica se o status code da resposta é 200