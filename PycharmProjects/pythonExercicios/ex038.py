cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

numero1= int(input('Favor digite o primeiro número:'))
numero2= int(input('Favor digite o segundo número:'))

if numero1 == numero2:
    print('Os Numeros {} e {} são {}'.format(numero1,numero2,cores['azul']+'Iguais'+cores['limpa']))
elif numero1 > numero2:
    print('o Numero {} é maior que {}'.format(numero1,numero2))
else:
    print('o Numero {} é maior que {}'.format(numero2,numero1))

    print(cores['azul'] + 'Olá Mundo' + cores['limpa'])
    #if (a+b) > c and (a+c) > b and (b+c) > a :
#    print('Os lados {}{}{},{},{} formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
#else:
#    print('Os lados {}{}{},{},{} nao formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
