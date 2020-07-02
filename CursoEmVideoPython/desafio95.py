scoult = dict()
gols = list()
time = list()
temp = 0
while True:
    scoult['Jogador'] = str(input('Qual o nome do jogador: '))
    scoult['Número partidas'] = int(input('Quantas partidas foram jogadas? '))
    for i in range(0,scoult['Número partidas']):
        gols.append(int(input(f'Quantos gols foram marcados na partida {i+1} de {scoult["Jogador"]}? ')))
    scoult['Gols'] = gols[:]
    for i in range(0,scoult['Número partidas']):
        if i == 0:
            scoult['Total de gols'] = gols[i]
        else:
            scoult['Total de gols'] += gols[i]
    time.append(scoult.copy())
    gols.clear()
    if str(input('Deseja continuar [S/N]? ')) in 'Nn':
        break
    print('-' * 50)
print('-' * 50)
print('{:^50}'.format('TABELO PERFORMANCE'))
print('-' * 50)
print('{:<5}{:<15}{:<25}{:<5}'.format('cod', 'Jogador', 'Gols', 'Total'))
for e in time:
    print('{:<5}{:<15}{:<25}{:<5}'.format(temp, e['Jogador'], str(e['Gols']), e['Total de gols']))
    temp += 1
print('-' * 50)
while True:
    temp = int(input('De aual jogador você deseja mais detalhes? [cod] 999 p/ sair. '))
    if temp == 999:
        break
    else:
        print(f'-- Performance do jogador: {time[temp]["Jogador"]}')
        for i in range(0,time[temp]["Número partidas"]):
            print(f'    => Na partida {i+1} {time[temp]["Jogador"]} marcou {time[temp]["Gols"][i]} vez(es).')
        print(f'Foi um total de {time[temp]["Total de gols"]} gols')
