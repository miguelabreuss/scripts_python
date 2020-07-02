print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
c1 = float(input('Digite o comprimento da primeira reta:[cm] '))
c2 = float(input('Digite o comprimento da segunda reta:[cm] '))
c3 = float(input('Digite o comprimento da terceira reta:[cm] '))
if c2 - c3 < c1 < c2 + c3 and c1 - c3 < c2 < c1 + c3 and c2 - c1 < c3 < c2 + c1:
    print('É UM TRIÂNGULO!')
    if c1 == c2 == c3:
        print('O triângulo é equilátero.')
    elif c1 == c2 or c2 == c3 or c1 == c3:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('NÃO É UM TRIÂNGULO!')