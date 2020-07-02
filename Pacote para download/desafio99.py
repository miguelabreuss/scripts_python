def maior(* num):
    m = 0
    print('-='*20)
    print('Analisando os valores passados...')
    for a in num:
        print(f'{a} ', end='')
        time.sleep(0.3)
        if a > m:
            m = a
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')
    time.sleep(0.5)


import time

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()