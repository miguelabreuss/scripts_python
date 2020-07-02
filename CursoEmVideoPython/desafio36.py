valor = float(input('Qual o valor do imóvel? [R$] '))
salario = float(input('Qual o seu salário atual bruto? [R$] '))
prazo = float(input('Em quanto tempo deseja quitar o finaciamento? [anos] '))

parcela = (valor / (prazo*12))
print('Parcela: R${:.2f}'.format(parcela))
percentual = ((valor / (prazo*12)) / salario) * 100
print('Percentual do salário comprometido: {:.2f}%'.format(percentual))

if percentual >= 30:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado. Passar no guichê.')