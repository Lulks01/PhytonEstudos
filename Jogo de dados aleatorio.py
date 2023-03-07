from random import randint
from time import sleep
from operator import itemgetter
ranking = ()
game = {'Jogador1':randint(1,6),'Jogador2':randint(1,6),'Jogador3':randint(1,6),'Jogador4':randint(1,6)}
print('Valores sorteados: ')
for k, v in game.items():
    print(f'{k} tirou: {v} no dado!')
    sleep(0.2)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('===='*5)
for i, v in enumerate(ranking):
    print(f'{1+1}° Lugar           : {v[0]} com {v[1]} Pontos     ')
    sleep(0.2)
