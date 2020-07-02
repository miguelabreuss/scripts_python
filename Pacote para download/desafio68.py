import random
n = comp = count = 0
pi = ''
print('-='*30)
print('JOGO DE PAR OU IMPAR!')
print('-='*30)
while True:
    n = int(input('Digite um número: '))
    pi = str(input('[P]ar ou [I]mpar? ')).lower()
    comp = random.randrange(10)
    if (n + comp) % 2 == 0 and pi == 'p':
        print(f'Você escolheu {n} e o computador {comp}. {n} + {comp} = {n+comp}, que é \33[4mPAR\33[m!')
        print('VITÓRIA! Vamos jogar novamente...')
        print('-='*30)
        count += 1
    elif (n + comp) % 2 != 0 and pi == 'i':
        print(f'Você escolheu {n} e o computador {comp}. {n} + {comp} = {n+comp}, que é \33[4mÍMPAR\33[m!')
        print('VITÓRIA! Vamos jogar novamente...')
        print('-=' * 30)
        count += 1
    else:
        print(f'Você escolheu {n} e o computador {comp}. {n} + {comp} = {n + comp}')
        print(f'\33[:31mVocê foi derrotado\33[m. Suas vitórias consecutivas foram \33[:34m{count}\33[m.')
        break
