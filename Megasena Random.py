import random
import time
lista = []
jogos = int(input('Quantos jogos você quer sortear?'))
print('='*25)
print('='*3, f'Sorteando {jogos} Jogos', '='*3)
print('='*25)
for c in range(0, jogos):
    lista.clear()
    time.sleep(1)
    for i in range(0, 6):
        lista.append(random.randint(1, 60))
    print(f'Jogo {c+1} {lista}')
