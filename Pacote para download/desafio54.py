import datetime
idade = 0
data = ''
count = 0

for i in range(0, 7):
    data = str(input('Digite a data de nascimento [dd/mm/aaaa] da {}ª pessoa: '.format(i+1)))
    data_format = datetime.date(int(data.split('/')[2]), int(data.split('/')[1]), int(data.split('/')[0]))
    idade = datetime.date.today() - data_format
    if idade.days > 7670:
        count += 1
print('{} pessoas são maiores de 21 anos e já podem fumar um beck!'.format(count))
