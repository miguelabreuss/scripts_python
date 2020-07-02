from datetime import date
ano = int(input('Em qual ano você nasceu? [XXXX] '))

idade = date.today().year - ano

if idade < 18:
    print('Você ainda vai se alistar. Faltam {} anos'.format(18 - idade))
elif idade > 18:
    print('Você já se alistou ou deveria ter feito isso {} anos atrás'.format(idade - 18))
else:
    print('Você se alistará este ano.')
