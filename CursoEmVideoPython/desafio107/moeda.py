def aumentar(valor, per=1, format=False):
    corrigido = '{:.2f}'.format(float(valor * (1 + per / 100)))
    if format == True:
        corrigido = moeda(corrigido)
    return corrigido


def diminuir(valor, per=1, format=False):
    corrigido = '{:.2f}'.format(float(valor * (1 - per / 100)))
    if format == True:
        corrigido = moeda(corrigido)
    return corrigido


def dobro(valor, format=False):
    corrigido = '{:.2f}'.format(float(valor * 2))
    if format == True:
        corrigido = moeda(corrigido)
    return corrigido


def metade(valor, format=False):
    corrigido = '{:.2f}'.format(float(valor / 2))
    if format == True:
        corrigido = moeda(corrigido)
    return corrigido

def moeda(valor):
    formatado = 'R${}'.format(str(valor).replace('.', ','))
    return formatado

def resumo(valor, aumento, reducao):
    print('='*32)
    print('{:^32}'.format('RESUMO DO VALOR'))
    print('='*32)
    print('{:<21}{:<}'.format('Preço analisado:', moeda(f'{valor:.2f}')))
    print('{:<21}{:<}'.format('Dobro do preço:', dobro(valor, True)))
    print('{:<21}{:<}'.format('Metade do preço:', metade(valor, True)))
    print('{:<21}{:<}'.format(f'{aumento}% de aumento', aumentar(valor, aumento, True)))
    print('{:<21}{:<}'.format(f'{reducao}% de redução', diminuir(valor, reducao, True)))
    print('='*32)
