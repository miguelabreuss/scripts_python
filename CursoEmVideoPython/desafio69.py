sexo = flag = ''

idade = count_h = count_m = count_maior = 0
while True:
    sexo = str(input('Digite o sexo [M/F]: ')).lower()
    idade = int(input('Digite a idade: '))
    print('-='*30)
    if sexo == 'm':
        count_h += 1
    if sexo == 'f' and idade < 21:
        count_m += 1
    if idade >= 18:
        count_maior +=1
    flag = str(input('Deseja continuar [S/N]? ')).lower()
    if flag == 'n':
        break
print(f'Foram cadastrados {count_h} homens, {count_m} mulheres com menos de 20 anos e {count_maior} pessoas com mais de 18 anos')
