def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('CONTADOR DE VOGAIS')

def vowel_counter(word):
    vowel = 0
    for i in word:
        if i in 'aeiouAEIOU':
            vowel += 1
    
    return print(f'A palavra {word} tem {vowel} vogais!')

word = str(input('Insira uma palavra: ')).strip()
if not word:
    print('Nenhuma palavra digitada!')
else:
    vowel_counter(word)