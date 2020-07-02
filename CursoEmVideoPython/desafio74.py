import random
maior = 0
menor = 999
sorteados = random.randrange(0,1000), random.randrange(0,1000), random.randrange(0,1000), random.randrange(0,1000), random.randrange(0,1000)
print(f'Os números sorteados são {sorteados}.')
for i in range(0,5):
    if sorteados[i] > maior:
        maior = sorteados[i]
    if menor > sorteados[i]:
        menor = sorteados[i]
print(f'O menor valor gerado foi {menor} e o maior foi {maior}')
# print(f'O menor valor gerado foi {min(sorteados)} e o maior foi {max(sorteados)}')