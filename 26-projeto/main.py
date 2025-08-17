def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

products_price = []

def product_catalog():
    print('Catalogo de produtos!')
    for product, price in products_price:
        print(f'Produto {product} | Preço R${price:.2f}')



menu('CATALOGO DE PRODUTOS')
print('Guarde nome de produtos e seus preço. Após finalizar você ira ver seu catalogo!')
while True:
    try:
        product = input('Insira o nome do produto: ').strip().title()
        price = float(input('Insira o preço do produto: '))
        products_price.append((product, price))
    except ValueError:
        print('ERRO: Valor inserido não corresponde!')
        continue
    c = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if c == 'S':
        continue
    elif c == 'N':
        menu('Resultado')
        product_catalog()
        break
    else:
        print('Escolha entre [S/N]!')
        