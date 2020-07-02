def notas(* num, sit=False):
    """
    -> Função que avalia o desempenho de uma determinada turma escolar
    :param num: uma ou várias notas dos alunos (aceita várias)
    :param sit: valor opcional que inclui, quando True, Situação da turma.
    :return: Dicionário com informações da turma analisada
    """
    global turma
    media = 0
    turma['Quantidade'] = len(num)
    turma['Maior Nota'] = max(num)
    turma['Menor Nota'] = min(num)
    for a in num:
        media += a
    media = media / len(num)
    turma['Nota Média'] = '{:.2f}'.format(media)
    if sit == True:
        if media < 6:
            turma['Situação'] = 'Ruim'
        elif 6 <= media <= 7:
            turma['Situação'] = 'Regular'
        else:
            turma['Situação'] = 'Boa'
    return turma


turma = dict()
notas(8, 4, 8, 6, 7, 9, sit=True)
print(turma)
help(notas)