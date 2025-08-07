def row(len = 35):
    print('-' * len)

def menu(msg):
    row()
    print(f'{msg:^35}')
    row()

from random import choice

words = [
    'Banana',
    'Maça',
    'Kiwi',
    'Abacaxi',
    'Abacate',
    'Melão',
    'Melancia',
    'Laranja',
    'Uva',
    'Morango',
    'Manga'
]

random_words = choice(words).upper()


def hangman_game():
    guessed_letters = [] # letras acertadas
    wrong_counter = 0 # letras erradas
    max_erros = 6
    print('Quantidade de palavras:')
    print('_'.replace('', ' ') * len(random_words))
    while True:
        text = str(input('Digite uma letra: ')).strip().upper()

        if not text or len(text) != 1 or not text.isalpha():
            print('Digite apenas uma LETRA')
            continue

        if text in guessed_letters:
            print('Você ja acertou essa letra')
            continue

        if text in random_words:
            guessed_letters.append(text)
            print(f'Você acertou uma letra: {text}')
        else:
            wrong_counter += 1
            print(f'Letra errada! Tentativas {max_erros - wrong_counter}')
            if wrong_counter >= max_erros:
                print('Você perdeu!')
                print(f'A palavra era {random_words}')
                break
        
        display = [letter if letter in guessed_letters else '_' for letter in random_words]
        print(' '.join(display))

        if '_' not in display:
            print('Parabens você adivinhou a palavra')
            break



menu('JOGO FORCA (VERSÃO FRUTAS)')
hangman_game()



