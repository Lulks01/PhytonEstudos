tot18 = toth = totm20 = tot = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    tot += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp =='N':
        break
print('Done')
print(f'Nesse grupo temos {tot18} pessoas maiores de 18 anos de {tot} Pessoas')
print(f'{toth} Homens')
print(f'E {totm20} Mulheres com menos de 20 anos')


