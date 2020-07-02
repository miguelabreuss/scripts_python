from random import randint
import time
jogos = []
premiados = []
sorteado = 0
print('='*40)
print('{:^40}'.format('JOGA MEGA SENA'))
print('='*40)
palpites = int(input('Quantos palpites deseja jogar? '))
print(f'-='*5, end='')
print('{:^20}'.format('SORTEANDO {} JOGOS'.format(palpites)), end='')
print(f'-='*5)
for i in range(0, palpites):
    for c in range(0, 6):
        while True:
            sorteado = randint(0, 60)
            if sorteado not in jogos:
                jogos.append(sorteado)
                break
    premiados.append(jogos[:])
    print(f'Jogo {i+1}: {sorted(premiados[i])}')
    time.sleep(2)
    jogos.clear()
print(f'-='*5, end='')
print('{:^20}'.format('BOA SORTE!'.format(palpites)), end='')
print(f'-='*5)