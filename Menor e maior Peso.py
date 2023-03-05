pessoas = []
temp = []
numcadastro = 0
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(pessoas) is 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    numcadastro += 1
    r = str(input('Deseja continuar? [S/N]')).upper().split()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]')).upper().split()[0]
    if r == 'N':
        break
print(f'Você cadastrou {numcadastro} pessoas')
print(f'O menor peso foi de {men}KG Peso de',end=' ')
for p in pessoas:
    if p[1] is mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO maior peso é de {mai}KG Peso de', end=' ')
for p in pessoas:
    if p[1] is men:
        print(f'[{p[0]}]', end=' ')
