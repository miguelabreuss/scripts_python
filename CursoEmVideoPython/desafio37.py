num = int(input('Digite o número a ser convertido: '))
alternativa = int(input('Digite [1] para binário, [2] para octal ou [3] para hexadecimal: '))
if alternativa == 1:
    bin_num = bin(num)
    print('O valor {} convertido para binário é {}'.format(num, bin_num))
elif alternativa == 2:
    oct_num = oct(num)
    print('O valor {} convertido para octal é {}'.format(num, oct_num))
elif alternativa == 3:
    hex_num = hex(num)
    print('O valor {} convertido para hexadecimal é {}'.format(num, hex_num))
else:
    print('Alternativa de conversão inválida.')
