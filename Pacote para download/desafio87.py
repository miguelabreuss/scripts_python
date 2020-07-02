matriz = []
linha = []
soma_pares = soma_terc = maior_seg = 0
for i in range(0, 3):
    for c in range(0, 3):
        linha.append(int(input(f'Digite o valor para a posição [{i},{c}]: ')))
    matriz.append(linha[:])
    linha.clear()
print('-='*30)
for i in range(0, 3):
    for c in range(0,3):
        if matriz[i][c] % 2 == 0:
            soma_pares += matriz[i][c]
        if c == 2:
            soma_terc += matriz[i][c]
        if i == 1 and matriz[i][c] > maior_seg:
            maior_seg = matriz[i][c]
        print(f'[ {matriz[i][c]} ]', end='')
    print('')
print('-='*30)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos números da terceira coluna é {soma_terc}.')
print(f'O maior número da segunda linha é {maior_seg}.')
