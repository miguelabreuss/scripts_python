grade = []
aluno = []
notas = []
medias = float()
while True:
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Digite primeira nota: ')))
    notas.append(float(input('Digite segunda nota: ')))
    aluno.append(notas[:])
    medias = (notas[0] + notas[1]) / 2
    aluno.append(medias)
    grade.append(aluno[:])
    if str(input('Deseja continuar [S/N]? ')).lower() == 'n':
        break
    notas.clear()
    aluno.clear()
print('-='*14)
print('{:^28}'.format('RESULTADO FINAL'))
print('-='*14)
print('No.   NOME           MÉDIA')
print('-'*28)
for i in range(0, len(grade)):
    print('{:<6}{:<15}{:.2f}'.format(i, grade[i][0], grade[i][2]))
print('-'*28)
while True:
    qual = int(input('Mostrar notas de qual aluno? (Invalide para sair) '))
    if qual < 0:
        break
    elif qual > (len(grade) - 1):
        break
    else:
        print(f'As notas de {grade[qual][0]} são {grade[qual][1]}.')
        print('')
