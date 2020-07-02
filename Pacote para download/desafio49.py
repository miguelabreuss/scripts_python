num = int(input('Digite o número que deseja saber a tabuada: '))
print('-='*21)
for i in range(1,10):
    print('{} x {} = {}'.format(num, i, num*i))
