from datetime import date
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

nascimento= int(input('Favor digite o ano de nascimento:'))
ano = date.today().year

if (ano-nascimento) <= 9:
    print('Você está na categoria Mirim pois nasceu tem {}{}{} anos'.format(cores['azul'],ano-nascimento,cores['limpa']))
elif (ano-nascimento) <= 14:
    print('Você está na categoria Infantil pois nasceu tem {}{}{} anos'.format(cores['azul'],ano-nascimento,cores['limpa']))
elif (ano-nascimento) <=19:
    print('Você está na categoria Junior pois nasceu tem {}{}{} anos'.format(cores['azul'],ano-nascimento,cores['limpa']))
elif (ano-nascimento) <=20:
    print('Você está na categoria Senior pois nasceu tem {}{}{} anos'.format(cores['azul'],ano-nascimento,cores['limpa']))
else:
    print('Você está na categoria Master pois nasceu tem {}{}{} anos'.format(cores['azul'],ano-nascimento,cores['limpa']))

    #if (a+b) > c and (a+c) > b and (b+c) > a :
#    print('Os lados {}{}{},{},{} formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
#else:
#    print('Os lados {}{}{},{},{} nao formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
