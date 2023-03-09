jogador = {}
time = []
partidas = []
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? : '))
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida N°{c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        print('ERRO! Digite S ou N')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('='*40)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}',end=' ')
print()
for k, v in enumerate(time):
    print(f'{k+1:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 Para interromper)')) 
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Jogador no código {busca} não cadastrado!')
    else:
        print(f'--- Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'      No jogo {i+1} fez {g} gols.')
        print('='*30)
print('Finalizado!')

    