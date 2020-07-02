matriz = []
linha = []
for i in range(0, 3):
    for c in range(0, 3):
        linha.append(int(input(f'Digite o valor para a posição [{i},{c}]: ')))
    matriz.append(linha[:])
    linha.clear()
print('-='*30)
for i in range(0, 3):
    for c in range(0,3):
        print(f'[ {matriz[i][c]} ]', end='')
    print('')
