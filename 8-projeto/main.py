def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg}')
    row()

menu('CALCULADORA DE MEDIA')

notes = []

for i in range(1, 4):
    try:
        note = float(input(f'Insira a {i}° nota: '))
        notes.append(note)
    except ValueError:
        print('ERRO: Valor inserido não é numerico')
        exit()

sum_notes = sum(notes)
average = sum_notes / 3

def mean(number):
    if number >= 7 and number <= 10:
        print('Aprovado!')
    elif number >= 5 and number < 7: 
        print('Recuperação')
    else:
        print('Reprovado')

mean(average)
