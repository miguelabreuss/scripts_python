from CursoEmVideoPython import titulo

def cadastro(nome, idade):
    f = open('pessoas_cadastradas.txt', 'a')
    f.write('\n')
    f.write(f'{nome:<22}{idade} anos')
    print(f'{nome} de {idade} anos cadastrado com sucesso')


def exibir():
    titulo.destaque('Pessoas cadastradas')
    f = open('pessoas_cadastradas.txt', 'r')
    for linha in f:
        print(linha, end='')
    print()


while True:
    titulo.destaque('Menu principal')
    print(f'\33[:32m1 - \33[:34mCadastrar nova pessoa')
    print(f'\33[:32m2 - \33[:34mVer pessoas cadastradas')
    print(f'\33[:32m3 - \33[:34mSair\33[m')
    titulo.linha(30)
    try:
        resp = int(input('\33[:32mQual o seu comando? \33[m'))
    except:
        print('\33[:31mOpção Inválida!\33[m')
    else:
        if resp == 1:
            while True:
                nome = str(input('Nome: '))
                if nome.isnumeric() == False and nome != '':
                    try:
                        idade = int(input('Idade: '))
                    except:
                        print('\33[:31mDigite uma idade válida!\33[m')
                    else:
                        cadastro(nome, idade)
                        break
                else:
                    print('\33[:31mDigite um nome válido!\33[m')
        elif resp == 2:
            exibir()
        elif resp == 3:
            titulo.destaque('Encerrando o programa...')
            break
        else:
            print('\33[:31mOpção Inválida!\33[m')
