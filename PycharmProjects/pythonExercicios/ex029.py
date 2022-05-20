velocidade = int(input('Favor Digite a Velocidade do Carro:'))
if velocidade>= 80:
    multa = (7*(velocidade-80))
    print ('Você foi multado em {} por estar a {}'.format(multa,velocidade))

