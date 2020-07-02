sexo = flag = ''
idade = count_h = count_m = count_maior = 0
while True:
    print('-'*30)
    print('CADASTRO DE NOVA PESSOA')
    print('-'*30)
    idade = int(input('Qual a idade? '))
    if idade >= 18:
        count_maior += 1
    while True:
        sexo = str(input('Qual o sexo [M/F]? ')).lower()
        if sexo == 'm':
            count_h += 1
            break
        elif sexo == 'f':
            if idade < 20:
                count_m += 1
            break
    while True:
        flag = str(input('Deseja continuar [S/N]? ')).lower()
        if flag in 'sn':
            break
    if flag == 'n':
        break
print('-'*60)
print('''FIM DOS CADASTRAMENTOS
''')
print(f'Foram cadastrados {count_h} homens.')
print(f'Dos cadastrados {count_maior} pessoas são maiores de 18 anos.')
print(f'Das mulheres cadastradas {count_m} são menores de 20 anos.')
