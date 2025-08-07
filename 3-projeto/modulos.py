def linha(tam = 45):
    print('-' * tam)

def menu(msg):
    linha()
    print(f'{msg:^30}')
    linha()

def escolha_pi(frase):
    if frase == 'PAR':
        print('Você escolheu par!')
    elif frase == 'IMPAR':
        print(f'Você escolheu impar!')
    else:
        print(f'Escolha entre PAR ou Impar!!')
        print('Inicie novamente o programa')
        exit()
