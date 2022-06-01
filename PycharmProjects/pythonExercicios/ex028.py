import random
from time import sleep
numero = int(input('Favor Digite um Numero:'))
randomico =  random.randint(0,5)
print('Processando...')
sleep(5)
if randomico== numero:
    print('-=-' * 20)
    print ('Você Acertou !')
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('Errou !')
    print('-=-' * 20)
