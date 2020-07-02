def manual(comando):
    print('\33[1:30:44m~' * 40)
    print('\33[1:30:44m{:^40}'.format(f"Acessando o manual do comando '{comando}'"))
    print('\33[1:30:44m~' * 40)
    print('\33[m', end='')
    print('\33[7:30m', end='')
    help(comando)
    print('\33[m', end='')


resp = ''
while True:
    print('\33[1:30:42m~'*25)
    print('\33[1:30:42m{:^25}'.format('SISTEMA DE AJUDA PyHELP'))
    print('\33[1:30:42m~'*25)
    resp = str(input('\33[mFunção ou Biblioteca > '))
    if resp == 'sair':
        print('\33[1:37:41m~' * 25)
        print('{:^25}'.format('ATÉ LOGO!'))
        print('~' * 25)
        print('\33[m', end='')
        break
    else:
        manual(resp)