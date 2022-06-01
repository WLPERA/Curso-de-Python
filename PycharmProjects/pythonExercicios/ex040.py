
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

nota1= float(input('Favor digite a primeira nota:'))
nota2= float(input('Favor digite a segunda nota:'))
media = (nota1+nota2)/2

if media >= 7:
    print('Você está aprovado com a media {}{:.2f}{}'.format(cores['azul'],media,cores['limpa']))
elif (media >=5 and media<7):
    print('Você está em recuperação com a media {}{:.2f}{}'.format(cores['azul'],media,cores['limpa']))
else:
    print('Você está reprovado com a media {}{:.2f}{}'.format(cores['azul'],media,cores['limpa']))

    #if (a+b) > c and (a+c) > b and (b+c) > a :
#    print('Os lados {}{}{},{},{} formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
#else:
#    print('Os lados {}{}{},{},{} nao formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
