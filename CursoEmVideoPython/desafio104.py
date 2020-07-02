def leiaInt(frase):
    while True:
        n = input(frase)
        if n.isnumeric() == True:
            return n
        else:
            print('\33[:31mERRO! Digite um número inteiro válido\33[m')


n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')