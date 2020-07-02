def área(larg, compr):
    area = larg * compr
    print('A área do terreno de {} m x {} m é de {:.2f} m².'.format(larg, compr, area))

# Programa principal
print('-' * 30)
print('{:^30}'.format('ANALISADOR DE TERRENOS'))
print('-' * 30)
l = float(input('Largura [m]: '))
c = float(input('Comprimento[m]: '))
área(l, c)