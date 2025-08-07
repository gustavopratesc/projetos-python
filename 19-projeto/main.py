from time import sleep


def count(second):
    for i in range(second, 0, -1):
        sleep(1)
        print(f'{i}')


seconds = int(input('Digite um tempo em segundos: '))
count(seconds)
print('⏰ Tempo esgotado!')