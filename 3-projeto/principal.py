from modulos import *
from random import randint

def sorteio(numero, escolha):
    computador = randint(0, 10)
    soma = numero + computador
    print(f'O computador jogou {computador}')
    print(f'Soma total {soma} -> {"PAR" if soma % 2 == 0 else "IMPAR"}')

    if soma % 2 == 0 and escolha == "PAR":
        print('VOCÊ GANHOU :)')
    elif soma % 2 == 1 and escolha == "IMPAR":
        print(f'VOCÊ GANHOU :)')
    else:
        print(f'Você perdeu!!')



# programa principal
menu('PAR OU IMPAR')
while True:
    escolha = str(input('Você quer? [PAR/IMPAR]: ')).strip().upper()
    escolha_pi(escolha)

    try:
        numero = int(input('Digite um número de 0 a 10: '))
        if 0 <= numero <= 10:
            sorteio(numero, escolha)
        else:
            print(f'Numero fora do intervalo permitido!')
    except ValueError:
        print(f'ERRO! Valor digitado não é um número inteiro!')
    
    while True:
        continuar = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in ['SIM', 'S', 'SI']:
            break
        elif continuar in ['NÃO', 'N', 'NAO']:
            print('Finalizando programa...')
            exit()
        else:
            print('Escolha entre [S/N]')
