soma = 0
count = 0
num = 0

for i in range(0, 6):
    num = int(input('Digite o {}º número: '.format(i + 1)))
    if num % 2 == 0:
        soma += num
        count += 1

print('Foram somados {} números, e o resultado foi {}.'.format(count, soma))
