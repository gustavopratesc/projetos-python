def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('CONTADOR DE LETRAS')

def letter_counter(text):
    letters = {
        "count_letter": 0
    }
    for _ in text:
        letters['count_letter'] += 1
    return print(f'Quantidade de palavras nesse texto é {letters["count_letter"]}')

text = input('Insira uma frase: ').strip().capitalize()
if not text:
    print('ERRO: Nenhuma frase digitada')
else:
    letter_counter(text)