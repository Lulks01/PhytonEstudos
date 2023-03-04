nuns = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
enter = 0
while True:
    enter = int(input('Digite um número entre 0 a 20: '))
    if enter > 20:
        print('Digite um valor valido')
        enter = int(input('Digite um número entre 0 a 20: '))
    print('O número digitado foi: ',nuns[enter])
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
print('Fim do programa')

