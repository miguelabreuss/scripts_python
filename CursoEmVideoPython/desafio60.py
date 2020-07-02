num = int(input('Digite um número qualquer: '))
result = 1
while num != 0:
    result *= num
    num -= 1
print('O fatorial é {}'.format(result))