nome = flag = mais_barato = ''
preco = total = count_prod = 0
menor_preco = 999999999999
while True:
    print('-' * 30)
    print('REGISTRAR NOVO PRODUTO')
    print('-' * 30)
    nome = str(input('Qual o nome do produto? '))
    preco = float(input(f'Qual o preço do produto {nome}? '))
    total += preco
    if preco >= 1000:
        count_prod +=1
    if preco < menor_preco:
        mais_barato = nome
        menor_preco = preco
    while True:
        flag = str(input('Deseja continuar [S/N]? '))
        if flag in 'SsNn':
            break
    if flag in 'Nn':
        break
print('-' * 30)
print('''RESULTADO DA COMPRA
''')
print(f'O total gasto na compra foi de \33[:31mR${total:.2f}\33[m.')
print(f'\33[:34m{count_prod}\33[m produtos encontrados acima de \33[4mR$1.000,00\33[m')
print(f'O produto mais barato foi \33[:32m{mais_barato}\33[m, que custa \33[:32mR${menor_preco:.2f}\33[m.')