alt = 0
while 0 <= alt < 5:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR')
    alt = int(input('Digite a operação ou [5] para sair: '))
    if alt == 1:
        num1 += num2
        print('O resultado da SOMA é {}.'.format(num1))
    elif alt == 2:
        num1 *= num2
        print('O resultado da MULTIPLICAÇÃO é {}.'.format(num1))
    elif alt == 3 and num1 < num2:
        num1 = num2
        print('O MAIOR número é {}.'.format(num1))
    elif alt > 5:
        alt = int(input('''\33[4:31mOpção inválida.\33[m
    O que você deseja?
    [4] NOVOS NÚMEROS
    [5] SAIR
    '''))
