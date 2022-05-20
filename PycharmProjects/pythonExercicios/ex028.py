import random
numero = int(input('Favor Digite um Numero:'))
randomico =  random.randint(0,5)
if randomico== numero:
    print ('Você Acertou !')
else:
    print('Errou !')
