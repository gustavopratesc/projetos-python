def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('Analisador de Notas')

set_of_notes = []

def note_analyzer(notes):
    max_notes = max(notes)
    min_notes = min(notes)
    average_notes = sum(notes) / len(notes)
    print(f'Nota maxima: {max_notes}')
    print(f'Nota minima: {min_notes}')
    print(f'Media das notas: {average_notes}')
    if average_notes >= 70:
        print('Excelente!')
    elif average_notes >= 60 and average_notes < 70:
        print('Bom!')
    elif average_notes >= 50 and average_notes < 60:
        print('Regular!')
    else:
        print('Pessimo!')

try:
    while True:
        notes = float(input('Insira a nota: '))
        set_of_notes.append(notes)
        while True:
            c = input('Quer continuar? [S/N]: ').strip().upper()[0]
            if c == 'S':
                break
            elif c == 'N':
                print('Respostas...')
                note_analyzer(set_of_notes)
                exit()
            else:
                print('Escolha entre [S/N]!!')
except ValueError:
    print('ERRO: Valor inserido não é númerico!')
