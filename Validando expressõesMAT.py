part = 0
w = []
w = str(input('Digite uma expressão:')).strip()
print(f'a expressão digitada foi: {w}')
size = len(w)
while True:
    for c in range(0,size):
        if w[c] in ')':
            part -=1
        if part < 0:
            print('Sua expressão está invalida')
            break
        if w[c] in '(':
            part +=1
    break
if part % 2 == 0:
    print('Sua expressão é válida!')
