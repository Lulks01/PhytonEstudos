from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}') 
    if p > 0:
        for c in range(i-1,f+1,p):
            print(f'{c}',end=' ', flush=True)
            sleep(0.1)
        print()
    else:
        for c in range(i,f-1,p):
            print(f'{c}',end=' ', flush=True)
            sleep(0.1)
    

contador(1,100,2)
contador(100,0,-2)
a = int(input('Digite de onde vai começar: '))
b = int(input('Digite até onde vai o contador: '))
c = int(input('Digite o Passo do contador: '))
contador(a,b,c)