idade = 0
idade_media = 0
maior_idade = 0
count_mulheres = 0
mais_velho = ''

for i in range(0, 4):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i+1)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i + 1)))
    sexo = str(input('Digite o sexo [M/F] da {}ª pessoa: '.format(i + 1)))
    idade_media += idade
    if sexo.lower() == "m" and idade > maior_idade:
        mais_velho = nome
        maior_idade = idade
    elif sexo.lower() == "f":
        if idade >= 21:
            count_mulheres += 1
print('A média de idade do grupo é \33[4m{:.2f}\33[m anos'.format(idade_media/4))
print('Foram cadastradas {} mulher(es) acima de 21 anos'.format(count_mulheres))
print('O homem mais velho é \33[4m{}\33[m com \33[4m{}\33[m anos'.format(mais_velho, maior_idade))