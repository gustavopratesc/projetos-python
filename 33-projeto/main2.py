def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('GERADOR DE SENHAS')

import random
import string
# string.ascii_letters → pega todas as letras (A–Z e a–z)
# string.digits → pega os números de 0 a 9
# string.punctuation -> pega caracteres especiais
characters = string.ascii_letters + string.digits + string.punctuation
size = int(input('Digite o tamanho da senha: '))
password = ''.join(random.choice(characters) for _ in range(size))

print(f'Sua senha gerada é: {password}')