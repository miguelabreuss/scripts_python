from datetime import date
ano = int(input('Em qual ano você nasceu? [XXXX] '))

idade = date.today().year - ano

if idade <= 9:
    print('Atleta mirim com {} anos'.format(idade))
elif 9 < idade <= 14:
    print('Atleta infantil com {} anos'.format(idade))
elif 14 < idade <= 19:
    print('Atleta junior com {} anos'.format(idade))
elif 19 < idade <= 20:
    print('Atleta sênior com {} anos'.format(idade))
else:
    print('Atleta master com {} anos'.format(idade))
