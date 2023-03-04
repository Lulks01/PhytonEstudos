import random
print('-==='*15)
print('BEM-VINDO AO JOGO DE PAR OU IMPAR')
wins = 0
tipo = ' '
print('-==='*15)
while tipo not in 'PI':
    tipo = str(input('Escolha entre Par ou Impar: [P/I] ')).strip().upper()[0]
while True:
    player = int(input('Digite um número de 0 à 10: '))
    system = random.randint(1,11)
    total = player + system
    print(f'Você jogou {player} e o computador {system}, total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            wins +=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            wins +=1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
if wins == 0:
    print('Você não ganhou nenhuma vez!')
else:
    print(f'Você ganhou {wins} vezes, mas infelizmente agora você perdeu!')
