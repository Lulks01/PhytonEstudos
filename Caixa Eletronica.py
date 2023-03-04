valor = int(input('Quanto dinheiro você quer sacar: R$'))
cedulas = [50, 20, 10, 1]
valorrestante = 0 
for x in range(0, 4):
    if valor - valorrestante > cedulas[x]:
        print(f'{(valor - valorrestante) // cedulas[x]} cédulas de {cedulas[x]} reais')
        valorrestante = (valor // cedulas[x]) * cedulas[x]