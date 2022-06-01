
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

preco = float(input('Favor digite o preco:'))
condicao= float(input('Favor digite a condicao (1=a vista,2=cartao,3=3 x no cartao,4=3x ou mais:'))
if condicao == 1:
    print('O preco {} a ser pago a vista é {}{:.2f}{}'.format(preco,cores['azul'],preco-(preco*10/100),cores['limpa']))
elif condicao==2:
    print('O preco {} a ser pago a vista no cartao {}{:.2f}{}'.format(preco,cores['azul'],preco-(preco*5/100),cores['limpa']))
elif condicao==3:
    print('O preco a ser pago a vista no cartao {}{:.2f}{}'.format(cores['azul'],preco,cores['limpa']))
else:
    print('O preco a ser pago em 3x no cartao é {}{:.2f}{}'.format(cores['azul'],preco+(preco*20/100),cores['limpa']))

    #if (a+b) > c and (a+c) > b and (b+c) > a :
#    print('Os lados {}{}{},{},{} formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
#else:
#    print('Os lados {}{}{},{},{} nao formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
