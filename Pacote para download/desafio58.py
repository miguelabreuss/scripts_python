import random
gerado = random.randrange(11)
count = 0
num = 11
while num != gerado:
    num = int(input('Digite um número entre 0 e 10: '))
    count += 1
print('Parabéns, você acertou o número {}! Foram {} tentativas realizadas.'.format(gerado, count))
