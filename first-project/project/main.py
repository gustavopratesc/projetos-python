from menu import *

menu_msg('BEM VINDO AO CAIXA ELETRONICO. INSIRA O VALOR QUE DESEJA SACAR EM R$')
try:
    saque = int(input('Insira o valor de saque: R$'))
    cedulas = [200, 100, 50, 20]

    if valor_retirada(saque):
        retirada(saque, cedulas)

except ValueError:
    print(f'Digite apenas números inteiros validos!')

