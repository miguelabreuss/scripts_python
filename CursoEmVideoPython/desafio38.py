a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

if a > b:
    print('O valor {} é maior que {}'.format(a, b))
elif a < b:
    print('O valor {} é maior que {}'.format(b, a))
else:
    print('{} é igual a {}'.format(a, b))
