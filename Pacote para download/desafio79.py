seq = []
num = 0
resp = ''
while True:
    num = int(input('Digite um valor: '))
    if num not in seq:
        seq.append(num)
    else:
        resp = str(input('Valor já encontrado na sequência. Deseja continuar [S/N]? '))
        if resp.lower() == 'n':
            break
print(f'Os valores registrados são: {sorted(seq)}')