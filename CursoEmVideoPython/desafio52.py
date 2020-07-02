num = int(input('Digite um número qualquer: '))
primo = 0

for i in range(2, num):
    if num % i == 0:
        primo = 1

if primo == 1:
    print('O número {} não é primo.'.format(num))
else:
    print('O número {} é primo.'.format(num))
