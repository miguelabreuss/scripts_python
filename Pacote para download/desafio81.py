lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    if str(input('Deseja continuar [S/N]? ').lower()) == 'n':
        break
print(f'Foram digitados {len(lista)} números.')
print(f'A lista com valores ordenados de forma decrescente é:  {sorted(lista, reverse=True)}.')
if 5 in lista:
    print(f'O valor 5 está na posição {lista.index(5)}.')
else:
    print(f'O valor 5 não foi digitado.')
