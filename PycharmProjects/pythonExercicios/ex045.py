
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

escolha1 = int(input('Digite 1 para Pedra, 2 para Tesoura, 3 Para Papel:'))
escolha2 = int(input('Digite 1 para Pedra, 2 para Tesoura, 3 Para Papel:'))
if escolha1==1:
    texto1='PEDRA'
elif escolha1==2:
    texto1='TESOURA'
else:
    texto1=='PAPEL'

if escolha2==1:
    texto2='PEDRA'
elif escolha2==2:
    texto2='TESOURA'
else:
    texto2='PAPEL'

if escolha1==escolha2:
    print('Empate {}{}{} com {}{}{}'.format(cores['azul'],texto1,cores['limpa'],cores['amarelo'],texto2,cores['limpa']))
elif escolha1 ==1 and escolha2 == 2:
    print('Deu pedra ! {}{}{} com {}{}{}'.format(cores['azul'],texto1,cores['limpa'],cores['amarelo'],texto2,cores['limpa']))
elif escolha1 ==1 and escolha2 == 3:
    print('Deu Papel ! {}{}{} com {}{}{}'.format(cores['azul'], texto1, cores['limpa'], cores['amarelo'], texto2,cores['limpa']))
elif escolha1==2 and escolha3 ==3:
    print('Deu Tesoura ! {}{}{} com {}{}{}'.format(cores['azul'], texto1, cores['limpa'], cores['amarelo'], texto2,
                                             cores['limpa']))

#if (a+b) > c and (a+c) > b and (b+c) > a :
#    print('Os lados {}{}{},{},{} formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
#else:
#    print('Os lados {}{}{},{},{} nao formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
