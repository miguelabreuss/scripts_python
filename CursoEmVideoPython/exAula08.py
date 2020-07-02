#  import math
from math import sqrt, ceil
#  from math import ceil
num = int(input('Digite um número que deseja saber a raiz: '))
#  raiz = math.sqrt(num)
raiz = sqrt(num)
#  arredondado = math.ceil(raiz)
arredondado = ceil(raiz)
print('O valor da raiz quadrada de {}, é {:.2f}. O valor arredondado para cima é {}'.format(num, raiz, arredondado))