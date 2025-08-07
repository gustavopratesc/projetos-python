def line(len = 70):
    print('-' * len)

def menu_msg(msg):
    line()
    print(f'     {msg}     ')
    line()


def valor_retirada(valor):
    if valor <= 0:
        print(f'Não é possivel sacar 0 ou valor negativo!')
    elif valor % 5 != 0:
        print(f'Insira um número valido (multiplo de 5)')
        return False
    else:
        print(f'Valor valido. Verificando cedulas disponiveis')
        return True


def retirada(valor, cedulas):
    print('\nNotas entregues:')
    for c in cedulas:
        qtd = valor // c
        if qtd > 0:
            print(f'{qtd} x R${c}')
            valor -= qtd * c