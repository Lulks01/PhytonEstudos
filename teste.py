resp = 'S'
tentativas = soma = media = maior = 0
num = int(input('Digite um valor: '))
menor = num
while resp in 'S':
    num = int(input('Digite um valor: '))
    soma += num
    if maior < num:
        maior = num
    elif menor > num:
        menor = num
    tentativas += 1
    media = soma/tentativas
    print('A média até agora é de {} de {} números digitados'.format(media, tentativas))
    resp = str(input('Quer continuar?' '[S/N]')).upper().strip()[0]
print('=-=='*20)
print('\033[32mForam digitados {} valores, e esses valores tem uma média de {}'.format(
    tentativas, media))
print('E o maior número digitado foi {} e o menor foi {}\033[m'.format(
    maior, menor))
print('=-=='*20)
