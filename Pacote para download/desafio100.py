def sorteio():
    for i in range(0, 5):
        num = randint(1, 10)
        print(f'{num} ', end='')
        numeros.append(num)
        time.sleep(0.5)
    print('PRONTO!')
def somaPar():
    sP = 0
    for a in numeros:
        if a % 2 == 0:
            sP += a
    print(sP)


from random import randint
import time

numeros = list()
print('Sorteando 5 valores: ', end='')
sorteio()
print(f'Somando os números pares em {numeros}, temos ', end='')
somaPar()


