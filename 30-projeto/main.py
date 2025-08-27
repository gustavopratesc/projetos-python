def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('TABUADA')

def multiplication_table(number):
    print(f'A tabuada do número {number}:')
    row()
    for i in range(1, 11):
        print(f'{number} x {i} = {number * i}')

try:
    number = int(input('Insira um número: '))
    multiplication_table(number)
except ValueError:
    print('ERRO: Valor inserido não é númerico!')
