from random import randint
from time import sleep

def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg}')
    row()

menu('SORTEIO NÚMEROS')

def luck(number):
    luck = [] # <-- precisou de uma lista
    print('Sorteando números...')
    for _ in range(5):
        number_luck = randint(1, 10)
        luck.append(number_luck)
        print(f'Numero sorteado: {number_luck}')
        sleep(0.3)

    row()
    print(f'Números sorteados: {luck}')

    if number in luck:
        print(f'Você acertou um número!! {number}')
    else:
        print(f'Infelizmente você não acertou nada.')

try:
    number = int(input('Insira um número de 1 a 10: '))
    if number < 0 or number > 10:
        print('ERRO: Digite entre 1 a 10')
    else:
        print('Resultados...')
        luck(number)
except ValueError:
    print('ERRO: Valor inserido não é inteiro númerico!')