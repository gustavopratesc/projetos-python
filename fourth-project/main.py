def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^25}')
    row()

menu('TABUADA NO TERMINAL')

def table(num):
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')

try:
    number = int(input('Insira um número: '))
    print(f'A tabuada de {number} é')
except ValueError:
    print(f'ERRO: Valor inserido não é um número!')

table(number)
