def row(len = 20):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^20}')
    row()

menu('CADASTRO USUARIO')


try:
    user = input('Cadastro de usuario: ').strip()
    if not user:
        print('Nenhuma entrada fornecida!')
        exit()
    password = input('Cadastro de senha: ').strip()
    if not password:
        print('Nenhuma entrada fornecida!')
        exit()
except EOFError:
    print('ERRO: Nenhuma entrada fornecida!')
    exit()

key = {
    "user": user,
    "password": password
}

menu('LOGIN')

def login(saved_user, saved_password):
    print('3 tentativas de login, se errar é bloquado o acesso!')
    attempts = 0
    while attempts < 3:
        input_user = input('Insira seu usuario: ').strip()
        input_password = input('Insira sua senha: ').strip()
        if input_user == saved_user and input_password == saved_password:
            print('Acesso liberado!!!')
            return
        else:
            attempts += 1
            print(f'Usuario e senha incorretos! Tentativas restantes {3 - attempts}')
    print('Acesso negado!')

login(key['user'], key['password'])
