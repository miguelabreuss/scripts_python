frase = str(input('Escreva a frase a ser analisada: '))
frase_format = frase.lower().replace(' ','')
palindromo = 1
for i in range(1, len(frase_format) + 1):
   if frase_format[i - 1] != frase_format[-i]:
       palindromo = 0
if palindromo == 1:
    print('A frase "{}" é um palíndromo'.format(frase))
else:
    print('A frase "{}" não é um palíndromo'.format(frase))