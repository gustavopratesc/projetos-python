def row(size = 30):
    print(f'-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('Soma de números até N')

def add_numbers(number):
    print(f'A soma de todos os números ate {number} é:')
    for i in range(1, number):
        print(f'{i + i}')
try:
    number = int(input('Insira um número: '))
    add_numbers(number)
except ValueError:
    print('ERRO: Insira um número inteiro')