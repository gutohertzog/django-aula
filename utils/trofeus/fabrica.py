# from inspect import signature
from random import randint

from faker import Faker


FAKE = Faker('pt_BR')


def rand_ratio():
    return randint(840, 900), randint(473, 573)


def cria_vitoria():
    return {
        'titulo': FAKE.sentence(nb_words=2),
        'descricao': FAKE.sentence(nb_words=12),
        'ano': randint(0000, 1499),
        'data_campeao': FAKE.date_time(),
        'tecnico': {
            'nome': FAKE.first_name(),
            'sobrenome': FAKE.last_name(),
        },
        'categoria': {
            'name': FAKE.word()
        },
        'foto': {
            'url': 'https://loremflickr.com/%s/%s/sport,soccer' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(cria_vitoria())
