from random import randint

def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

number_random = randint(1, 20)
        

while True:
    try:
        number = int(input('Insira um número de 1 a 20 para tentar adivinhar: '))
        if number > number_random:
            print('Menos')
        elif number < number_random:
            print('Mais')
        else:
            print('ACERTOU!!!!!!!')
            break
    except ValueError:
        print('ERRO: valor digitado não é inteiro númerico')
        continue