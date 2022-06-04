import random
from time import sleep
randomico = 0
numero = 1
palpites = 0
while randomico != numero:
    numero = int(input('Favor Digite um Numero:'))
    randomico =  random.randint(0,5)
    print('Processando...')
    sleep(5)
    palpites += 1
    if randomico==numero:
        print('-=-' * 20)
        print ('Você Acertou !')
        print('-=-' * 20)
        break
    else:
        print('-=-' * 20)
        print('Errou !')
        print('-=-' * 20)

print ('Foram necessários {} palpites para acertar'.format(palpites))