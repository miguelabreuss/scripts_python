maior_peso = 0
menor_peso = 999
cadastro = []
dados = []
lista_maipeso = []
lista_menpeso = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    cadastro.append(dados[:])
    if dados[1] > maior_peso:
        maior_peso = dados[1]
    elif dados[1] < menor_peso:
        menor_peso = dados[1]
    dados.clear()
    if str(input('Deseja continuar [S/N]? ').lower()) == 'n':
        break
print(f'Foram cadastradas {len(cadastro)} pessoas.')
for p in cadastro:
    if p[1] == maior_peso:
        lista_maipeso.append(p[0])
    if p[1] == menor_peso:
        lista_menpeso.append(p[0])
print(f'As pessoas com menor peso são {lista_menpeso} com {menor_peso} kg.')
print(f'As pessoas com maior peso são {lista_maipeso} com {maior_peso} kg.')