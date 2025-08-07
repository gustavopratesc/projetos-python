def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^20}')
    row()

menu('CONVERSOR DE TEMPERATURA')

def menu_temperature():
    print(f""" 
            1- Celsius -> Fahrenheit
            2- Fahrenheit -> Celsius
            """)
menu_temperature()

try:
    choice = int(input('Insira a opção '))
    if choice > 2:
        print('Erro: não existe essa opção')
        exit()
    temperature = float(input('Insira a temperatura: '))
except ValueError:
    print('ERRO: O valor digitado não é um numero!')


def conversion(choice, temperature):
    if choice == 1:
        fah = (temperature * 9/5) + 32
        print(f'A temperatura C°{temperature} convertido em F°{fah:.2f}')
    elif choice == 2:
        cel = (temperature - 32) * 5/9
        print(f'A temperatura F°{temperature} convertido em C°{cel:.2f}')

conversion(choice, temperature)