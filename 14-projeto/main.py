def row(len = 30):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('CALCULADORA DE IMC')

def bmi(weight, height):
    bmi = weight / height**2
    if bmi < 18.5:
        return print('Magreza')
    elif 18.5 <= bmi <= 24.9:
        return print('Normal')
    elif 25 <= bmi <= 29.9:
        return print('Sobrepeso')
    else:
        return print('Obesidade')

try:
    weight = float(input('Insira seu peso: '))
    height = float(input('Insira sua altura: '))
except ValueError:
    print('ERRO: Não o valor inserido não é númerico!')
    
bmi(weight, height)