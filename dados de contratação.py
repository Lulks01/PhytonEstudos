from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
born = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - born
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Sálario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('='*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')