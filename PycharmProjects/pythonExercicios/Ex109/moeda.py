def aumentar(preco = 0,taxa = 0, formato=False):
    res = preco + (preco * taxa/100)
    return res if format is False else moeda(res)

def diminuir(preco=0,taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if format is False else moeda(res)

def dobro(preco = 0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco = 0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco =0, moeda = 'R$ '):
    return f'{moeda}{preco:>.2f}'.replace('.',',')

def resumo(preco=0,taxaa=10,taxar=5):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preco analisado : \t\t{moeda(preco)}')
    print(f'Dobro do preco: \t\t{dobro(preco,True)}')
    print(f'Metade do preco: \t\t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco,taxaa,True)}')
    print(f'Com {taxar}% de aumento: \t\t{diminuir(preco, taxar, True)}')
    print('-' * 30)
