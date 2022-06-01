from datetime import date
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

nascimento= int(input('Favor digite o ano de nascimento:'))
ano = date.today().year

if (ano-18) == nascimento:
    print('Você deve ser alistar neste ano pois nasceu em {}{}{}'.format(cores['azul'],nascimento,cores['limpa']))
elif (ano-18) < nascimento:
    print('Falta {}{}{} anos para o alistamento '.format(cores['azul'],nascimento-(ano-18),cores['limpa']))
else:
    print('Você está atrasado passou {}{}{} anos do alistamento'.format(cores['azul'],(ano-nascimento)-18,cores['limpa']))

    #if (a+b) > c and (a+c) > b and (b+c) > a :
#    print('Os lados {}{}{},{},{} formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
#else:
#    print('Os lados {}{}{},{},{} nao formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
