def row(len = 25):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^20}')
    row()

menu('TO-DO-LIST')
print("""
        1- Adicionar
        2- Listar
        3- Remover
        4- Sair
""")
def menu_option(number):
    add = []
    while True:
        if number == 1:
            menu('ADICIONAR')
            while True:
                toadd = input('Insira a tarefa que você quer adicioanr a lista: ').strip()
                done_input = input('Ja fez? [S/N]: ').strip().upper()
                done = True if done_input == 'S' else False

                task = {
                    "descricao": toadd,
                    "feito": done
                }
                add.append(task)

                advance = str(input('Quer inserir mais na lista? [S/N]: ')).strip().upper()[0]
                if advance != 'S':
                    break
            number = int(input('Digite a opção do menu (1 - 4): '))
        elif number == 2:
            menu('LISTANDO TAREFAS')
            if not add:
                print('Nenhuma tarefa definida!')
            else:
                for i, v in enumerate(add):
                    status = 'feito' if v['feito'] else 'Pendente'
                    print(f'{i + 1}. {v["descricao"]} - {status} ')
            number = int(input('Digite a opção do menu (1 - 4): '))
        elif number == 3:
            menu('REMOVER')
            if not add:
                print('Nenhuma tarefa para remover!')
            else:
                print(f'Qual deseja remover?')
                for i, v in enumerate(add):
                    print(f'{i + 1}° | {v["descricao"]} | {v["feito"]}')
                try:
                    remove = int(input('Insira o indice em que quer remover: '))
                    if 1 <= remove <= len(add):
                        add.pop(remove - 1)
                        print('Tarefa removida')
                    else:
                        print('Número invalido')
                except ValueError:
                    print('ERRO: Entrada invalida!')
            number = int(input('Digite a opção do menu (1 - 4): '))

        elif number == 4:
            menu('PROGRAMA FINALIZADO')
            break
        else:
            print('Escolha entre 1 a 4')


try:
    option = int(input('Selecione uma opção: '))
    if option < 0:
        print('ERRO: Opção invalida! Renicie o programa')
        exit()
except ValueError:
    print('ERRO: O valor inserido não é um número inteiro!')

menu_option(option)