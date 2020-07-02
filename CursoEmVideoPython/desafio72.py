extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    num = int(input('Digite o número que deseja por extenso [0-20]: '))
    if num > 20 or num < 0:
        print('Número não encontrado')
        break
    else:
        print(f'Você escolheu o número {extenso[num]}.')
