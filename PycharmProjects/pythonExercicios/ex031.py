distancia = int(input('Favor Digite a distancia da viagem:'))
passagem = distancia * 0.50
if distancia<201:
    passagem = distancia * 0.50
    print ('o preco da passagem para a distancia {} é {}'.format(distancia,passagem))
else:
    passagem = distancia * 0.45
    print ('o preco da passagem para a distancia {} é {}'.format(distancia,passagem))
