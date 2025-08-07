def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg}')
    row()

menu('VERIFICADOR DE NÚMEROS PRIMOS')

def prime_numbers(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        print(f'Esse número {number} é primo!')
    else:
        print(f'Não é!')

try:
    number = int(input('Insira um número: '))
    if number < 0:
        print('ERRO: Digite um número maior que ZERO')
    else:
        prime_numbers(number)
except ValueError:
    print('ERRO: Valor inserido não é númerico!')