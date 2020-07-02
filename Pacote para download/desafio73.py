times = 'Flamengo', 'Cruzeiro', 'São Paulo', 'Corinthians', 'Botafogo', 'Atlético-MG', 'Chapecoense', 'Vasco', 'Bahia', 'Sport', 'Internacional', 'Santos', 'Athletico-PR', 'Figueirense', 'Grêmio', 'Palmeiras', 'Fortaleza', 'Goiás', 'Fluminense', 'CSA'
print('Os 5 primeiros colocados são: ')
for i in range(0, 5):
    print(f'{i + 1}º - {times[i]}')
print('-' * 30)
print('Os 4 últimos colocados são: ')
for i in range(-1, -5, -1):
    print(f'{i + 21}º - {times[i]}')
print('-' * 30)
print('Os clubes em ordem alfabética são: ', end='')
print(sorted(times))
print('-' * 30)
print(f'O \33[4:34mChapecoense\33[m está na {times.index("Chapecoense")+1}ª posição')