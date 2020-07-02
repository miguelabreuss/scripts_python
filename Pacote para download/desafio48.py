agr = 0
cont = 0
for a in range(0, 500, 3):
    if a % 2 != 0:
        print(a)
        agr += a
        cont += 1
print('O somatório desejado é {}. Foram somados {} números.'.format(agr, cont))