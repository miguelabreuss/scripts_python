palavras = 'forA', 'bolsonaro', 'miliciano', 'queiroz', 'laranja', 'flavio', \
           'bananinha', 'python', 'divertido', 'flamengo', 'bangu'
frase = ''
for i in range(0, len(palavras)):
    frase = 'Na palavra {} temos '
    for c in range(0, len(palavras[i])):
        if palavras[i][c].lower() == 'a':
            frase += 'a '
        elif palavras[i][c].lower() == 'e':
            frase += 'e '
        elif palavras[i][c].lower() == 'i':
            frase += 'i '
        elif palavras[i][c].lower() == 'o':
            frase += 'o '
        elif palavras[i][c].lower() == 'u':
            frase += 'u '
    print(frase.format(palavras[i].upper()))