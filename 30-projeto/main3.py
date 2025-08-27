def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('PAR OU IMPAR')

def even_or_odd(number):
    if number % 2 == 0:
        print(f'Esse número {number} é par')
    else:
        print(F'Esse número {number} é impar')

try:
    number = int(input('Insira um número: '))
    even_or_odd(number)
except ValueError:
    print('ERRO: Valor digitado não é inteiro númerico!')