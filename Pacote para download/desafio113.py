def leiaInt(frase):
    while True:
        try:
            n = int(input(frase))
        except:
            print('\33[:31mERRO! Digite um número inteiro válido\33[m')
        else:
            return n


def leiaFloat(frase):
    while True:
        try:
            n = float(input(frase))
        except:
            print('\33[:31mERRO! Digite um número do tipo float válido\33[m')
        else:
            return n


n = leiaFloat('Digite um float: ')
print(f'Você digitou o número {n:.2f}.')
n = leiaInt('Digite um número inteiro válido: ')
print(f'Você digitou o número inteiro {n}.')
