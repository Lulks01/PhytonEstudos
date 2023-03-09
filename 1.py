Person_register = {}
list_persons = []
soma_idades = media = 0
while True:
    list_persons.clear
    Person_register['nome'] = str(input('Nome: '))
    Person_register['sexo'] = str(input('Sexo: [M/F]')).upper().split()[0]
    while Person_register['sexo'] not in 'MF':
        print('ERRO! DIGITE M OU F!')
        Person_register['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
    Person_register['idade'] = int(input('Idade: '))
    soma_idades +=Person_register['idade']
    list_persons.append(Person_register.copy())
    resp = str(input('Quer continuar? [S/N]  ')).upper().split()[0]
    while resp not in 'S/N':
        print('Erro! Responda S ou N')
        resp = str(input('Quer continuar? [S/N]  ')).upper().split()[0]
    if resp == 'N':
        break
print(f' Foram cadastrados {len(list_persons)} pessoas')
media = soma_idades / len(list_persons)
print(f'A média das idades é : {media:5.2f} anos.')
print(f'As mulheres cadastradas foram :',end='')
for p in list_persons:
    if p['sexo'] is 'F':
        print(f'{p["nome"]}', end='')
print()
print(f'Lista das pessoas que estão acima da média', end='')
for p in list_persons:
    if p['idade'] >= media:
        print('       ')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
