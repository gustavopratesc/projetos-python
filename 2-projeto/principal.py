from modulos import *

menu('CONTADOR DE VOGAIS!')
frase = str(input('Insira uma palavra ou frase: ')).strip().lower()
numero_vogal = contador_vogal(frase)

print(f'O número de vogais dessa frase "{frase.capitalize()}" é {numero_vogal}')