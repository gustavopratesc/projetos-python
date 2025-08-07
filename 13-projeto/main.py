def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^20}')
    row()

menu('VERIFICADOR DE PALINDROMO')

def palindrome(text):
    new_text = text.replace(' ', '')
    inverted = new_text[::-1]
    if new_text == inverted:
        print(f'A frase {text} é um palindromo {inverted}')
    else:
        print('Não é!!')

text = input('Insira alguma frase ou palavra: ').strip().lower()

if not any(char.isalpha() for char in text):
    print(f'Erro: valor digitado não é uma frase!')
else:
    palindrome(text)