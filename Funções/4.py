from random import randrange
from time import sleep
nuns = []
def random():
    print(f'Os números Aleatórios sorteados foram:')
    for c in range(0, 10):
        nuns.append(randrange(0, 20, 1))
    print(nuns)
def dobra():
    pares = 0
    print('Pares dos números sorteados:')
    for c in range(0, len(nuns)):
        if nuns[c] % 2 == 0:
            print(nuns[c], end=' ')
            pares += nuns[c]
    print(f'\nA soma dos valores pares da lista {nuns} é: {pares}')


random()
sleep(1)
dobra()
