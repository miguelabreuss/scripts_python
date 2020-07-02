peso = 0
maior = 0
menor = 9999
pes_maior = 0
pes_menor = 0

for i in range(0, 5):
    peso = int(input('Digite o peso [kg] da {}ª pessoa: '.format(i+1)))
    if peso > maior:
        maior = peso
        pes_maior = i
    if peso < menor:
        menor = peso
        pes_menor = i
print('O maior peso lido foi {} kg, da {}ª pessoa'.format(maior, pes_maior + 1))
print('O menor peso lido foi {} kg, da {}ª pessoa'.format(menor, pes_menor + 1))