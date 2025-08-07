def row(len = 30):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^20}')
    row()

from num2words import num2words

menu('NÚMEROS EXTENSOS')

number = int(input('Insira um número inteiro para ver ele em forma extensa: '))
number_extensive = num2words(number, lang='pt_BR')

print(f'Número em forma de inteiro: {number} | Número em extenso: {number_extensive}')