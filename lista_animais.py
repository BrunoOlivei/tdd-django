lista_animais = [
    {'nome_animal':'urso','predador': True,'venenoso': 'False','domestico': False},
    {'nome_animal':'javali','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'búfalo','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'guepardo','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'molusco','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'caranguejo','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'lagostim','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'corvo','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'golfinho','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'pomba','predador': False,'venenoso': False,'domestico': True},
    {'nome_animal':'pato','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'elefante','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'flamingo','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'pulga','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'rã','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'morcego-da-fruta','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'girafa','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'mosquito','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'bode','predador': False,'venenoso': False,'domestico': True},
    {'nome_animal':'gorila','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'gaivota','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'hadoque','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'hamster','predador': False,'venenoso': False,'domestico': True},
    {'nome_animal':'falcão','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'abelha','predador': False,'venenoso': True,'domestico': True},
    {'nome_animal':'mosca','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'joaninha','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'leopardo','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'leão','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'lagosta','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'lince','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'salamandra','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'polvo','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'gambá','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'órix','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'avestruz','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'periquito','predador': False,'venenoso': False,'domestico': True},
    {'nome_animal':'pinguim','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'faisão','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'pique','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'piranha','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'ornitorrinco','predador': True,'venenoso': True,'domestico': False},
    {'nome_animal':'doninha','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'pónei','predador': False,'venenoso': False,'domestico': True},
    {'nome_animal':'toninha','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'puma','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'gato','predador': True,'venenoso': False,'domestico': True},
    {'nome_animal':'guaxinim','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'rena','predador': False,'venenoso': False,'domestico': True},
    {'nome_animal':'ema','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'escorpião','predador': True,'venenoso': True,'domestico': False},
    {'nome_animal':'cavalo marinho','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'leão marinho','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'verme','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'lesma','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'pardal','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'esquilo','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'estrela do Mar','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'arraia','predador': True,'venenoso': True,'domestico': False},
    {'nome_animal':'cisne','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'cupim','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'sapo','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'tartaruga','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'tuatara','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'atum','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'abutre','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'vespa','predador': False,'venenoso': True,'domestico': False},
    {'nome_animal':'lobo','predador': True,'venenoso': False,'domestico': False},
    {'nome_animal':'minhoca','predador': False,'venenoso': False,'domestico': False},
    {'nome_animal':'carriça','predador': False,'venenoso': False,'domestico': False}
]

import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from animais.models import Animal

def gerando_animais():
    for animal in lista_animais:
        nome = animal['nome_animal']
        predador = animal['predador']
        venenoso = animal['venenoso']
        domestico = animal['domestico']
        animal = Animal(nome=nome, predador=predador, venenoso=venenoso, domestico=domestico)
        animal.save()

gerando_animais()
print('animais gerados')