def contador(i, f, p):
    print('-=' * 20)
    if p == 0:
        p = 1
    if p > 0:
        if i > f:
            p = -p
            f = f - 1
            print(f'Contagem de {i} até {f + 1} de {-p} em {-p}')
        else:
            f = f + 1
            print(f'Contagem de {i} até {f - 1} de {p} em {p}')
    else:
        if i > f:
            f = f - 1
            print(f'Contagem de {i} até {f + 1} de {-p} em {-p}')
        else:
            p = -p
            f = f + 1
            print(f'Contagem de {i} até {f - 1} de {p} em {p}')
    for a in range(i, f, p):
        print(f'{a} ', end='')
        time.sleep(0.5)
    print('FIM!')


import time

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
