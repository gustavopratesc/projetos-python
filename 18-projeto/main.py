import random
from time import sleep

def row(len = 30):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^20}')
    row()

def menu_display():
    menu('SIMULADOR DE DADOS DE RPG')
    print('Tipos de dados disponiveis.')
    print('[1] D4   [2] D6    [3] D8   [4] D10')
    print('[5] D12  [6] D20   [7] Sair')

available_data = {
    '1': 4,
    '2': 6,
    '3': 8,
    '4': 10,
    '5': 12,
    '6': 20
}

def roll_dice(sides):
    return random.randint(1, sides)

menu_display()

while True:
    try:
        option = input('Insira a opção que deseja: ').strip()

        if option == '7':
            print('Programa finalizado!')
            break

        elif option in available_data:
            sides = available_data[option]
            print('Rolando dado...')
            sleep(0.8)
            resultado = roll_dice(sides)
            print(f'🎲 Você rolou um {resultado} no D{sides}!')

            while True:
                c = input('Quer continuar? [S/N]: ').strip().upper()[0]
                if c == 'S':
                    menu_display()
                    break
                elif c == 'N':
                    print('Programa finalizado.')
                    exit()
                else:
                    print('Resposta inválida. Digite apenas [S] ou [N].')

        else:
            print('Opção inválida! Tente novamente.')

    except ValueError:
        print('ERRO: Valor inserido não é válido!')