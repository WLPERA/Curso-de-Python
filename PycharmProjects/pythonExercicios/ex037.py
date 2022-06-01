cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

numero= int(input('Favor digite um número:'))
base = int(input('Favor digite a base de conversao 1=Binario,2=Octal,3=Hexadecimal:'))
if base == 1:
    print('o Numero {} em binário é : {}{}{} '.format(numero,cores['azul'],bin(numero),cores['limpa']))
elif base == 2:
    print('o Numero {} em octal é : {}{}{} '.format(numero, cores['azul'],oct(numero),cores['limpa']))
elif base == 3:
    print('o Numero {} em hexadecimal é : {}{}{} '.format(numero, cores['azul'],hex(numero),cores['limpa']))
else:
    print('Favor escolher entre 1 e 3')


    #if (a+b) > c and (a+c) > b and (b+c) > a :
#    print('Os lados {}{}{},{},{} formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
#else:
#    print('Os lados {}{}{},{},{} nao formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
