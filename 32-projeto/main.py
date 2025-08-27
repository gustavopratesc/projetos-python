def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

list_numbers = []

def show_numbers(list):
    print(f'O maior número da lista é: {max(list)}')
    print(f'O menor número da lista é: {min(list)}')

try:
    for i in range(5):
        number = int(input(f'Digite o {i + 1}° numero: '))
        list_numbers.append(number)
    show_numbers(list_numbers)
except ValueError:
    print(f'ERRO: Valor digitado não é inteiro númerico!')