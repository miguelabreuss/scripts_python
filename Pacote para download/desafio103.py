def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gol(s) na temporada')

jogador = str(input('Qual o nome do jogador? '))
gols = str(input('Quantos gols foram marcados? '))

if jogador == '':
    if gols == '':
        ficha('<desconhecido>', '0')
    else:
        ficha('<desconhecido>', gols)
else:
    ficha(jogador, gols)
