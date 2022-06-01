
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

peso = float(input('Favor digite o peso:'))
altura= float(input('Favor digite a altura:'))
imc = (peso/(altura**2))
if imc <= 18.5:
    print('Você está abaixo do peso com imc {}{:.2f}{}'.format(cores['azul'],imc,cores['limpa']))
elif (imc >18.5 and imc<=25):
    print('Você está no peso ideal com imc {}{:.2f}{}'.format(cores['azul'],imc,cores['limpa']))
elif (imc >25 and imc<=30):
    print('Você está no sobrepeso com imc {}{:.2f}{}'.format(cores['azul'],imc,cores['limpa']))
elif (imc >30 and imc<=40):
    print('Você está no obesidade com imc {}{:.2f}{}'.format(cores['azul'],imc,cores['limpa']))
else:
    print('Você está com obesidade morbida com imc {}{:.2f}{}'.format(cores['azul'],imc,cores['limpa']))

    #if (a+b) > c and (a+c) > b and (b+c) > a :
#    print('Os lados {}{}{},{},{} formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
#else:
#    print('Os lados {}{}{},{},{} nao formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
