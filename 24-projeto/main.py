# Gerenciador de Compras Simples
# Objetivo: Criar um programa que permita ao usuário adicionar itens a uma lista de compras, remover itens e visualizar a lista final.
# Funcionalidades:
# Adicionar itens — O usuário digita o nome do produto e ele é adicionado à lista.
# Remover itens — O usuário pode remover um item pelo nome.
# Exibir lista — Mostrar todos os itens atuais da lista.
# Encerrar programa — Finalizar quando o usuário escolher.
# Requisitos Técnicos:
# Usar listas para armazenar os itens.
# Usar laços (while) para manter o programa rodando até a saída.
# Usar condições (if/elif/else) para controlar o menu.
# Usar funções para cada ação (ex.: adicionar_item(), remover_item(), mostrar_lista()).

def row(size = 35):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^35}')
    row()

menu('Gerenciador de Compras Simples')
print("""
    1- Adicionar
    2- Remover
    3- Exibir
    4- Encerrar
""")

added_products = []

def add_product():
    while True:
        product = input('Insira o nome do produto: ').strip().capitalize()
        added_products.append(product)  
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in ['S', 'SIM']:
            continue
        elif c in ['N', 'NÃO', 'NAO']:
            break
        else:
            print('ERRO: Insira entre: [S/N]')

def remove_product():
    while True:
        if not added_products:
            print('Nenhum item na lista para ser removido!')
            return
        
        remove_name = input('Remova o nome do produto pelo nome: ').strip().capitalize()

        if remove_name in added_products:
            added_products.remove(remove_name)
            print(f'Produto removido: {remove_name}')
            break
        else:
            print(f'Produto não encontrado na lista')

def display_product():
    for i, v in enumerate(added_products):
        print(f'{i + 1}° | Nome: {v}')

# programa principal
while True:
    try:
        option = int(input('Insira a opção do menu: '))
        if not option:
            print('Nenhum valor inserido')
        if option == 1:
            add_product()
        elif option == 2:
            remove_product()
        elif option == 3:
            display_product()
        elif option == 4:
            print('Programa finalizado!')
            exit()
        else:
            print('ERRO: Insira entre 1 a 4')
    except ValueError:
        print('ERRO: Valor inserido não é númerico!')
