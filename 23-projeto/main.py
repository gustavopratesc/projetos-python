def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('VALIDADOR DE LOGIN')


def registration_login(user, password):
    if len(password) < 8:
        print('Poucos caracteres para a senha!')
        exit()
    return {"user": user, "password": password}


user = input('Cadastre seu usuario: ').strip()
password = input('Cadastre a sua senha: ').strip()
if not user:
    print('Nenhum valor digitado para usuario!')
    exit()

if not password:
    print('Nenhum valor digitado para senha!')
    exit()

registration_login(user, password)

menu('Login')

user_data = registration_login(user, password)

def login(login_user, login_password, user_data):
    for i in range(3):
        if login_user == user_data["user"] and login_password == user_data["password"]:
            print('Login validado com sucesso!')
            break
        else:
            remaining = 2 - i
            if remaining >= 0:
                print(f'Credenciais incorretas! Tentativas restantes {remaining}')
            
            if remaining < 0:
                print('Conta bloqueada!!!!')
            exit
        login_user = input('Insira seu usuario de login: ').strip()
        login_password = input('Insira sua senha de login: ').strip()
            

login_user = input('Insira seu usuario de login: ').strip()
login_password = input('Insira sua senha de login: ').strip()

if not login_user:
    print('Nenhum valor inserido para o login!')
    exit()

if not login_password:
    print('Nenhum valor inserido para o login!')
    exit()

login(login_user, login_password, user_data)