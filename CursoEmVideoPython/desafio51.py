a0 = int(input('Digite o primeiro termo da progressão aritmética: '))
termos = int(input('Digite quantos termos deseja exibir: '))
razao = int(input('Digite qual é a razão da progressão aritmética: '))
an = 0
print('A progressão final é:')
for i in range(0, termos * razao, razao):
    an = a0 + i
    print(an)
