velocidade = float(input('Favor Digite a Velocidade do Carro:'))
print('Tenha um bom dia e dirija com segurança')
if velocidade>= 80:
    multa = (7*(velocidade-80))
    print ('Você foi multado em {} por estar a {}'.format(multa,velocidade))