lista = []
while True:
    n = int(input('Digite o valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado!, Esse valor não será adicionado a lista')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'NS':
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'N':
        break
print('='*30)
lista.sort()
print(f'Você digitou os valores {lista}')