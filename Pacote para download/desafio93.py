scoult = dict()
gols = list\
    ()
scoult['Jogador'] = str(input('Qual o nome do jogador: '))
scoult['Número partidas'] = int(input('Quantas partidas foram jogadas? '))
for i in range(0,scoult['Número partidas']):
    gols.append(int(input(f'Quantos gols marcados na partida {i+1}? ')))
scoult['Gols'] = gols[:]
for i in range(0,scoult['Número partidas']):
    if i == 0:
        scoult['Total de gols'] = gols[i]
    else:
        scoult['Total de gols'] += gols[i]
print('-='*20)
print(scoult)
print('-='*20)
for k, v in scoult.items():
    print(f'{k} é {v}')
print('-=' * 20)
print(f'O jogador {scoult["Jogador"]} jogou {scoult["Número partidas"]} jogos.')
for i in range(0,scoult["Número partidas"]):
    print(f'    => Na partida {i+1} marcou {gols[i]} vez(es).')
print(f'Foi um total de {scoult["Total de gols"]} gols')
