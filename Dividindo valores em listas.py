full_list = []
par_list = []
impar_list = []
while True:
    qt = int(input('Quantos valores você quer digitar?'))
    for c in range(0,qt):
        full_list.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break

for c in range(0,len(full_list)):
    if full_list[c] % 2 == 0:
        par_list.append(full_list[c])
    else:
        impar_list.append(full_list[c])
full_list.sort
par_list.sort
impar_list.sort
print(f'Lista completa: {full_list}')
print(f'Lista de pares digitados {par_list}')
print(f'Lista de impares digitados {impar_list}')