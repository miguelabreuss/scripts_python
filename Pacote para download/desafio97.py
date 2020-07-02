def escreva(text):
    tam = len(text) + 6
    print(f'\33[:34m~\33[m'* (tam))
    print('{:^{}}'.format(text, tam))
    print(f'\33[:34m~\33[m' * (tam))


escreva('Curso em vídeo')
escreva('Olá Mundo!')
escreva('Miguel Abreu de Souza e Silva')