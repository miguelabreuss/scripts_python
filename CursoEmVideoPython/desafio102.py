def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: número a ser calculado.
    :param show: [optional] Mostrar ou não a decomposição fatorial
    :return: O valor do fatorial de um número num
    """
    c = 1
    if show == True:
        for i in range(0, num):
            if i == num - 1:
                print(f'{num - i} = ', end='')
            else:
                print(f'{num - i} x ', end='')
            c *= (i+1)
        print(c)
    else:
        for i in range(0, num):
            c *= (i+1)
        print(c)

# Programa principal
fatorial(10, show=True)
help(fatorial)
