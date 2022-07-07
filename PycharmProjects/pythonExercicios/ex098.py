from time import sleep

def contagem(i,f,p):
    if p<0:
        p*=-1
    if p ==0:
        p=1

    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end = '', flush=True)
            sleep(0.5)
            cont += p
        print('Fim !')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim !')

contagem(0,100,10)
contagem(10,0,2)

print('Agora é sua vez de personalizar a contagem:')
ini=int(input('Inicio: '))
fim=int(input('Fim:'))
passo=int(input('Passo:'))
contagem(ini,fim,passo)