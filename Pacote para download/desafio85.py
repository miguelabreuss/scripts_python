pares = []
impares = []
numeros = []

for i in range(0,7):
    numeros.append(int(input(f'Digite o {i+1}º valor: ')))
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])
print(f'Os números digitados foram {sorted(numeros)}, sendo os pares {sorted(pares)} e os ímpares {sorted(impares)}')