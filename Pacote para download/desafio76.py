precos = ('Mouse', 56.90, 'Teclado', 99.90, 'iPhone 11 Pro Max', 6999.90, 'Mochila Notebook', 235.60, 'CD RW', 0.60, 'DVD RW', 1.50, 'Cabo HDMI', 89.90)
total = 0
print('-=-'*20)
print('{:^60}'.format('LISTA DE PREÇOS'))
print('-=-'*20)
for i in range(0,len(precos),2):
    print('{:.<51}{}{:>7.2f}'.format(precos[i], 'R$', precos[i+1]))
    total += precos[i+1]
print('-'*60)
print('{:.<51}R${:>7.2f}'.format('Total', total))