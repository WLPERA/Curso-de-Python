
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

a = int(input('Favor digite o lado a do triangulo:'))
b = int(input('Favor digite o lado b do triangulo:'))
c = int(input('Favor digite o lado c do triangulo:'))

if (a+b) > c and (a+c) > b and (b+c) > a :
    print('Os lados {}{}{},{},{} formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
else:
    print('Os lados {}{}{},{},{} nao formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
