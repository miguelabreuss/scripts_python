count = soma = num = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        count += 1
print('A soma de {} números digitados é {}.'.format(count, soma))