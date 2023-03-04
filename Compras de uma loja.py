print('='*20)
print('SUPER ATACADO MERCALOJA')
print('='*20)
total = totalmil = n = lowv = 0
lowp = ' '
while True:
    produto = str(input('Nome do Produto:'))
    valor = float(input('Valor do produto: R$'))
    total += valor
    while n == 0:
        lowv = valor
        lowp = produto
        n = 1
    if valor < lowv:
        lowv = valor
        lowp = produto
    if valor > 1000:
        totalmil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra é de {total:.2f}R$')
print(f'Temos {totalmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato é {lowp} e custa {lowv:.2f}R$')

