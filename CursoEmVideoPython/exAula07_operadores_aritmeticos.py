n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
adc = n1 + n2
sub = n1 - n2
pro = n1 * n2
pot = n1 ** n2
div = n1 / n2
div_int = n1 // n2
rest = n1 % n2
print('A soma de {} e {} é {},\na subtração é {},\no produto é {}\ne a divisão é {:.3f}'.format(n1, n2, adc, sub, pro, div))
print('A potência entre {} e {} é {}, a divisão inteira é {} '.format(n1, n2, pot, div_int), end='')
print('e o resto é {}'.format(rest))
