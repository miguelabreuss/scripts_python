import random
num = int(input('Digite um número entre 0 e 5: '))
gerado = random.randrange(6)
print('O número gerado automaticamente é {}'.format(gerado))
if gerado == num:
    print('Parabéns! Você acertou o número gerado.')
else:
    print('Errou! Tente novamente.')
