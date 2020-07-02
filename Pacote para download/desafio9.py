n = int(input('Digite o número que deseja saber a tabuada: '))
print('')
i = 1
print('Tabuada do +')
while i <= 9:
    r = n + i
    print('{} + {} = {}'.format(n, i, r))
    i += 1
print('='*100)
print('Tabuada do -')
i = 1
while i <= 9:
    r = n - i
    print('{} - {} = {}'.format(n, i, r))
    i += 1
print('='*100)
print('Tabuada do *')
i = 1
while i <= 9:
    r = n * i
    print('{} * {} = {}'.format(n, i, r))
    i += 1
print('='*100)
print('Tabuada do /')
i = 1
while i <= 9:
    r = n / i
    print('{} / {} = {:.2f}'.format(n, i, r))
    i += 1