n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = float((n1 + n2) / 2)

if media < 5:
    print('Aluno \33[0:31mreprovado\33[m com média {:.1f} insuficiente.'.format(media))
elif 5 <= media < 7:
    print('Aluno em \33[0:33mrecuperação\33[m com média {:.1f}'.format(media))
else:
    print('Aluno \33[0:32mAPROVADO\33[m com média {:.1f}'.format(media))