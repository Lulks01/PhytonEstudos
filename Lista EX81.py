lista = []
while True:
    qt = int(input('Quantos valores você quer digitar?'))
    for c in range(0, qt):
        lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer adicionar mais valores? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        str(input('Quer adicionar mais valores? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print(f'Foram digitados {len(lista)} números nessa lista')
if 5 in lista:
    print('O valor 5 foi inserido nessa lista')
else:
    print('Não há um valor 5 nessa lista!')
lista.sort(reverse=True)
print(lista)
