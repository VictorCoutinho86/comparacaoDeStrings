""""
    Sistema criado a partir dos comentarios disponibilizados no Stackoverflow no link
    https://pt.stackoverflow.com/questions/217152/como-comparar-se-o-conte%c3%bado-de
    -duas-colunas-string-de-um-data-frame-s%c3%a3o-parecida?newreg=
    19fea371ae1340e4887ada3d8d1eead8
    Sobre o topico: Como comparar se o conteúdo de duas colunas string
    de um data frame são parecidas
"""
# coding: utf-8
# from unidecode import unidecode
from difflib import SequenceMatcher

ignore_list = ['de', 'do', 'da', 'dos', 'das']


def parse_name(full_name):
    name_list = full_name.split()  # Separa cada nome
    new_name_list = []
    for name in name_list:  # Percorre cada nome
        name = name.strip('.')  # Remove pontos
        name = name.strip(',')
        name = name.strip('/')
        name = name.strip('(')
        name = name.strip(')')
        name = name.strip('0 - 9')
        name = name.lower()  # Converte todas as letras em minúsculas
        if name in ignore_list:  # Remove preposições
            continue
        # name = unidecode(name.decode('utf8'))  # Remove acentos (necessita da biblioteca 'unidecode')
        new_name_list.append(name)
    return new_name_list


def is_similar(a, b):
    a = parse_name(a)
    b = parse_name(b)
    if len(a) != len(b):  # Se o número de palavras for diferente, retorna falso
        return False
    for x, y in zip(a, b):
        if (len(x) == 1) or (len(y) == 1):  # Se uma das palavras possuir apenas uma letra...
            if x[0] != y[0]:  # ...compara apenas a primeira letra
                return False
        else:  # Caso contrário...
            if x != y:  # ...compara a palavra toda
                return False
    return True  # Se todas as palavras forem iguais, retorna verdadeiro


# Testando taxa de similaridade
def sml(x, y):
    return SequenceMatcher(None, x, y).ratio()

    # x = 'José Luiz da Silva'
    # y = 'José L. Silva'
    #msg = "Taxa de similaridade "

    #print(msg, 'entre x e y: ', sml(x,y) )
    # print(msg, 'entre x e x: ', sml(x,x) )
