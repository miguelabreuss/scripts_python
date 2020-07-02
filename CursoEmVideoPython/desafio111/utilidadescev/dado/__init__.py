def leiaDinheiro(frase):
    while True:
        n = input(frase)
        if (n.isnumeric() or n.count('.') == 1 or n.count(',') == 1) and n != '.' and n != ',':
            n = n.replace(',', '.')
            return float(n)
        else:
            print(f'\33[:31mERRO! "{n}" é um valor inválido\33[m')