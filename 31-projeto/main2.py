def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('INVERSOR DE PALAVRAS')

def word_changer(word):
    word_modified = word[::-1]
    return print(word_modified)

word = str(input('Insira a palavra: ')).strip()
if not word:
    print('ERRO: Nenhuma palavra digitada!')
else:
    word_changer(word)