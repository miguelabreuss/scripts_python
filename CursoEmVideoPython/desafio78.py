seq = []
for i in range(0,5):
    seq.append(int(input(f'Digite o {i+1}º valor: ')))
print(f'Os valores digitados foram: {seq}')
print(f'O maior valor é {max(seq)} na(s) prosição(ões): ', end='')
for pos, num in enumerate(seq):
    if num == max(seq):
        print(f'{pos} ', end='')
print('')
print(f'O menor valor é {min(seq)} na(s) prosição(ões): ', end='')
for pos, num in enumerate(seq):
    if num == min(seq):
        print(f'{pos} ', end='')