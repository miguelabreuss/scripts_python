pessoa = dict()
galera = list()
media_idade = 0
mulheres = list()
acima_idade = list()
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: '))
    media_idade += pessoa['Idade']
    if pessoa['Sexo'] in 'fF':
        mulheres.append(pessoa.copy())
    galera.append(pessoa.copy())
    if str(input('Deseja continuar [S/N]? ')) in 'Nn':
        break
print('-='*25)
print(f'Foram cadastradas {len(galera)} pessoas.')
print(f'A média de idade da galera é {media_idade / len(galera)} anos.')
print(f'As mulheres cadastradas são ', end='')
for e in mulheres:
    print(f'{e["Nome"]} ', end='')
print('')
for e in galera:
    if e['Idade'] > (media_idade/len(galera)):
        acima_idade.append(e.copy())
print(f'As pessoas com idade acima da média são:')
for e in acima_idade:
    print(f'O nome é {e["Nome"]}, o sexo é {e["Sexo"].upper()} e a idade é {e["Idade"]}')
