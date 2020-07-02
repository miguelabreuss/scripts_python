classe = list()
aluno = dict()

aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7.5:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = '\33[:31mReprovado\33[m'
classe.append(aluno.copy())
for e in classe:
    for k,v in e.items():
        print(f'{k} é igual a {v}')
# print(classe)