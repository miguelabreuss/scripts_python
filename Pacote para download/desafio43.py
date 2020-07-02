altura = float(input('Qual a sua altura? [m] '))
peso = float(input('Qual o seu peso? [kg] '))
genero = input('Qual o seu gênero? [M - Masculino / F - Feminino] ')

imc = peso / (altura ** 2)

if genero.lower() == 'm':
    if imc < 20:
        print('O seu Índice de Massa Corporal é {:.2f}, considerado abaixo do normal.'.format(imc))
    elif 20 <= imc < 25:
        print('O seu Índice de Massa Corporal é {:.2f}, considerado normal.'.format(imc))
    elif 25 <= imc < 30:
        print('O seu Índice de Massa Corporal é {:.2f}, considerado obesidade leve.'.format(imc))
    elif 30 <= imc < 40:
        print('O seu Índice de Massa Corporal é {:.2f}, considerado obesidade moderada.'.format(imc))
    elif 40 <= imc:
        print('O seu Índice de Massa Corporal é {:.2f}, considerado obesidade mórbida.'.format(imc))
elif genero.lower() == 'f':
    if imc < 19:
        print('O seu Índice de Massa Corporal é {:.2f}, considerado abaixo do normal.'.format(imc))
    elif 19 <= imc < 24:
        print('O seu Índice de Massa Corporal é {:.2f}, considerado normal.'.format(imc))
    elif 24 <= imc < 29:
        print('O seu Índice de Massa Corporal é {:.2f}, considerado obesidade leve.'.format(imc))
    elif 29 <= imc < 39:
        print('O seu Índice de Massa Corporal é {:.2f}, considerado obesidade moderada.'.format(imc))
    elif 39 <= imc:
        print('O seu Índice de Massa Corporal é {:.2f}, considerado obesidade mórbida.'.format(imc))
else:
    print('Genêro não informado. Reinicie e informe F para feminino ou M para masculino.')