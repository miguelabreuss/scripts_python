seq = int(input('Digite o primeiro número: ')),\
      int(input('Digite o segundo número: ')),\
      int(input('Digite o terceiro número: ')),\
      int(input('Digite o quarto número: '))
print(f'O número 9 apareceu {seq.count(9)} vez(es)')
if 3 in seq:
    print(f'O número 3 aparece primeiro na posição {seq.index(3)+1}.')
else:
    print('O número 3 não consta na sequência.')
print(f'Os números pares da sequência são: ', end='')
for i in range(0,4):
    if seq[i] % 2 == 0:
        print(f'{seq[i]} ', end='')
