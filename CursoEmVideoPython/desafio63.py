n = int(input('Entre com a quantidade de termos da sequância: '))
an = [0, 1]
if n > 1:
    while n - 2 > 0:
        an.append(an[-1] + an[-2])
        n -= 1
    print('A sequência de Fibonacci solicitada é: {}'.format(an))
else:
    print('A sequência de Fibonacci solicitada é: {}'.format(an[0:1]))