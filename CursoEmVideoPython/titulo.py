def destaque(frase, tamanho=30):
    if tamanho != 30:
        tam = len(frase) + tamanho
    else:
        tam = 30
    print('=' * tam)
    print(f'{frase.upper():^{tam}}')
    print('=' * tam)

def linha(tamanho=25):
    print('=' * tamanho)