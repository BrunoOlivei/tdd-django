from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        '''Função que configura os atributos para os testes'''
        self.browser = webdriver.Firefox('/home/bruno/Documentos/tdd-django/') # Firefox

    def tearDown(self):
        '''Função para encerrar os servidores e o browser'''
        self.browser.quit() # Fecha o 
        
    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuário encontra um animal pesquisando.
        Vini deseja encontrar um novo animal para adotar. 
        Ele encontra o “Busca Animal” e decide usar o site, porque vê no menu do site escrito “Busca Animal”. 
        Já que ele quer adotar um animal.
        Ele vê um campo para pesquisar animais pelo nome
        Ele pesquisa por Leão e clica no botão pesquisar.
        O site exibe 4 caracteristicas do animal pesquisado.
        Ele desiste de adotar um leão e decide adotar um cachorro.
        """
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
