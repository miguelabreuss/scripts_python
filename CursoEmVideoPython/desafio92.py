import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
cadastro['Idade'] = (datetime.date.today().year - int(input('Ano de Nascimento: ')))
cadastro['Carteira'] = int(input('Carteira de Trabalho: '))
if cadastro['Carteira'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] - (datetime.date.today().year - cadastro['Idade'])) + 35
print('-'*35)
for k, v in cadastro.items():
    print(f'{k} é {v}')