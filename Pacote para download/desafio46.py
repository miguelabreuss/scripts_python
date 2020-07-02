import emoji
import time
num = int(input('Digite o número para contagem regressiva: '))

for num in range(num, 0, -1):
    print(num)
    time.sleep(1)
print('-='*7)
print(emoji.emojize('    \33[0:31mFIM!\33[m :fireworks:'))
print('-='*7)