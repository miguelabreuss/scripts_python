count = 0
soma = 0
num = 0
maior = 0
menor = 999999999999999999999999
resp = ''
while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Deseja continuar [S/N]: '))
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    count += 1
print('O MAIOR número digitado foi {}, o MENOR foi {} e a média foi {}'.format(maior, menor, soma / count))