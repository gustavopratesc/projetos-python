def row(len = 45):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^40}')
    row()

menu('CALCULADORA FATORIAL')

def factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        print(f'{factorial} x {i} = {factorial * i}')
        factorial *= i
    print(f'Fatorial de {number} é {factorial}')
        


try:
    number = int(input('Insira um número: '))
except ValueError:
    print('ERRO: Valor inserido não é inteiro númerico!')

factorial(number)