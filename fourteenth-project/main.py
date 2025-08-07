def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg}')
    row()

import string
import random

# ascii_letters = letras maiusculas e minusculas
# digitis = numeros de 0 a 9
# punctuation = simbolos como !@#$

# choice = aleatoriar
# sample = aleatoriar

def password(text):
    modified_password = string.ascii_letters + string.digits + string.punctuation # não sabia que tinha como fazer essa junção
    password = ''.join(random.sample(modified_password, text))
    return print(f'Sua senha gerada: {password}')


size_password = int(input('Digite a quantidade de caracteres que você quer na senha: '))
password(size_password)