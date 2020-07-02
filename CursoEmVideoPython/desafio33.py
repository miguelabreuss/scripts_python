n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
# Verificando maior
if n1 > n2 > n3:
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3
# Verificando menor
if n1 < n2 < n3:
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3
# Imprimindo resultados
print('O MAIOR número é {}'.format(maior))
print('O MENOR número é {}'.format(menor))