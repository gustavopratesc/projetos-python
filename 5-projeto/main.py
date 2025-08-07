def row(len = 45):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^20}')
    row()

menu('CONTADOR DE LETRAS MAIUSCULAS E MINUSCULAS')

def counter(text):
    uppercase = 0
    lowercase = 0
    for letter in text:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1
    return f'A contagem de letras: Maiusculas {uppercase} | Minusculas {lowercase}'


text = input('Insira um texto ou uma frase: ').strip()

if not any(char.isalpha() for char in text):
    print('ERRO: Valor digitado não é uma letra ou frase!')
else:
    print(f'A quantidade de cada palavra é: ')
    print(counter(text))

