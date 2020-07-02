vel = int(input('Qual a velocidade registrada? [km/h] '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Multa devida: R${},00'.format(multa))
else:
    print('Okay!')
