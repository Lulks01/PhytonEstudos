matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = scol3 = l2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}], [{c}]: '))
        if matriz[l][c] % 2 is 0:
            par += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='  ')
    print()
print(f'A soma dos valores pares é {par}')
for l in range(0, 3):
    scol3 += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol3}')
for c in range(0, 3):
    if c is 0:
        l2 = matriz[1][c]
    if l2 < matriz[1][c]:
        l2 = matriz[1][c]

print(f'A soma da segunda linha é {l2}')
