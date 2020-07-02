n = 0
while True:
    n = int(input('Digite o número que deseja ver a tabuada (negativo para parar): '))
    if n < 0:
        print('-=' * 40)
        print('Programa de tabuada encerrando. Volte sempre!')
        break
    for i in range(1,11):
        print(f'{n} x {i} = {i*n}')
    print('-='*40)
