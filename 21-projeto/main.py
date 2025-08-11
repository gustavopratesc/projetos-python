def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()
    
menu('VALIDAÇÃO DE CPF')

def validate_cpf(number):
    if len(number) == 11:
        print('CPF: Validado com sucesso!')
    else:
        print('CPF não validado!')
    

    

cpf = str(input('Insira seu CPF sem pontos nem caracteres: '))
if not cpf:
    print('ERRO: Nenhum valor inserido!')

validate_cpf(cpf)