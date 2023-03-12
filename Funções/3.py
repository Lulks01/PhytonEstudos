from time import sleep
def maior(*num):
    cont = maior = 0
    print('='*30)
    print('Analisando os números passados...')
    for n in num:
        print(f'{n:>3}', end=' ', flush=True)
        sleep(0.2)
    print(f'\nForam digitados {len(num)} valores')
    if num == ():
        print('Nenhum valor digitado!')
    else:
        print(f'O maior valor digitado foi {max(num)}')
        print('='*30)
    print('\n')


maior()
maior(3, 2, 5, 3)
maior(9, 7, 2, 1)
