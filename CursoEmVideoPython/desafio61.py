a0 = int(input('Digite o primeiro termo da progressão aritmética: '))
termos = int(input('Digite quantos termos deseja exibir: '))
razao = int(input('Digite qual é a razão da progressão aritmética: '))
an = [a0]
while termos > 1:
    an.append(an[-1] + razao)
    termos -= 1
print('A progressão final é: {}'.format(an))