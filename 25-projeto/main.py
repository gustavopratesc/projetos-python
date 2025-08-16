def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('LISTA DE COMPRAS')

list_item = []

def add_item():
        item = input('Insira o item: ').strip().title()
        list_item.append(item)
        if item in list_item:
            print(f'{item} adicionado a lista!')

def show_item():
    if list_item:
        for i, v in enumerate(list_item):
            print(f'{i + 1}° | Produto: {v}')
    else:
        print('Nenhum item adicionado ainda!')    
        
def delete_item():
    name_item = input('Insira o nome do produto em que quer remover: ').strip().title()
    if name_item in list_item:
        list_item.remove(name_item)
        print(f'Item {name_item} removido com sucesso!')
    else:
        print('Item não encontrado na lista!')


print('''
    1 - Adicionar
    2 - Listar
    3 - Remover
    4 - Sair
''')

while True:
    try:
        option = int(input('Digite uma das opções: '))
        if option == 1:
            add_item()
        elif option == 2:
            show_item()
        elif option == 3:
            delete_item()
        elif option == 4:
            print('Programa finalizado!')
            break
        else:
            print('Escolha entre 1 a 4')
    except ValueError:
        print('ERRO: Valor digitado incorreto!')
