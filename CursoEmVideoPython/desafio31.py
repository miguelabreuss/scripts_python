dist = float(input('Qual a distância percorrida? [km] '))
if dist <= 200:
    preco = float(dist * 0.5)
    print('O valor a pagar é R${:.2f}'.format(preco))
else:
    preco = float(dist * 0.45)
    print('O valor a pagar é R${:.2f}. Você teve um desconto de 10%!'.format(preco))
