def row(len = 45):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^40}')
    row()

menu('CONTADOR DE PALAVRAS')

def count_text(text):
    modified_text = text
    count = 0
    for p in modified_text:
        if not p:
            break
        else:
            count += 1
    
    print(f'A quantidade de palavras dessa frase é: {count}')
    return
#  programa principal

text = input('Insira qualquer palavra ou frase: ')
if not text:
    print('ERRO: Não inseriu nada!')
    exit()

count_text(text)



