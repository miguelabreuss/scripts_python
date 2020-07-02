lista = []
impares = []
pares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    if str(input('Deseja continuar [S/N]? ').lower()) == 'n':
        break
for termos in lista:
    if termos % 2 == 0:
        pares.append(termos)
    else:
        impares.append(termos)
print(f'A lista registrada é: {lista}')
print(f'Os valores pares da lista são {pares} e os ímpares são {impares}')