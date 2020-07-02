n = count = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    count += 1
    s += n
print(f'A soma dos {count} números digitados é {s}')