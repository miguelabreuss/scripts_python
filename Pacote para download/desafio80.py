seq = []
num = 0
for i in range(0,5):
    num = int(input(f'Digite o {i+1}º valor: '))
    if i == 0 or seq[-1] < num:
        seq.append(num)
    m = 0
    while m < i:
        if seq[m] > num:
            seq.insert(m, num)
            break
        m +=1
print(f'A sequência digitada foi: {seq}')
