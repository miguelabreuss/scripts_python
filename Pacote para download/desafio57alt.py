sexo = 'a'
while sexo not in 'MmFf':
    sexo = str(input('Digite o sexo [M/F] do usuário: '))
print('Obrigado por informar o sexo do usuário: {}.'.format(sexo.upper()))