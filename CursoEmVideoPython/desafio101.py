def voto(ano):
    idade = 0
    res = ''
    idade = datetime.today().year - ano
    if idade < 16:
        res = f'Com {idade} anos o voto é NEGADO'
    elif 16 <= idade < 18 or idade > 69:
        res = f'Com {idade} anos o voto é OPCIONAL'
    else:
        res = f'Com {idade} anos o voto é OBRIGATÓRIO PARA ALFABETIZADOS.'
    return res

from datetime import datetime

print(voto(int(input("Qual o ano de nascimento? "))))
