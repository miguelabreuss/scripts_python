from random import randint
import time
rodada = list()
jogada = dict()
m = 0
print('VALORES SORTEADOS:')
for i in range(0, 4):
    jogada['Jogador'] = f'jogador{i + 1}'
    jogada['Número'] = randint(1, 6)
    print(f'    O {jogada["Jogador"]} tirou {jogada["Número"]}.')
    time.sleep(1)
    rodada.append(jogada.copy())
print('-'*35)
print('RANKING DOS JOGADORES:')
for i in range(0, 4):
    num = rodada[i]['Número']
    if i != 0:
        while m < i:
            if rodada[m]['Número'] < num:
                rodada.insert(m, rodada[i].copy())
                rodada.pop(i + 1)
                break
            m += 1
    m = 0
for i in range(0, 4):
    print(f'    {i + 1}º Lugar - {rodada[i]["Jogador"]} tirou {rodada[i]["Número"]}')
