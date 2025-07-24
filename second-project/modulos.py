def linha(tam = 30):
    print('-' * tam)

def menu(msg):
    linha()
    print(f'{msg:^30}')
    linha()

def contador_vogal(frase):
    cont_vogal = 0
    vogais = 'aeiou'
    for v in frase:
        if v in vogais:
            cont_vogal += 1
    return cont_vogal