from django.test import TestCase, RequestFactory
from animais.models import Animal


class AnimalModelTestCase(TestCase):
    """Teste para o modelo Animal"""
    def setUp(self):
        self.animal = Animal.objects.create(
            nome='Leão',
            predador=True,
            venenoso=False,
            domestico=False
        ) # Cria um animal com as caracteristicas passadas
    
    def test_animal_cadastrado_com_caracteristicas(self):
        """Teste para ver se o animal está cadastrado com suas caracteristicas"""
        self.assertEqual(self.animal.nome, 'Leão') # Verifica se o nome do animal é Leão