a = int(input('Favor digite o lado a do triangulo:'))
b = int(input('Favor digite o lado b do triangulo:'))
c = int(input('Favor digite o lado c do triangulo:'))

if (a+b) > c and (a+c) > b and (b+c) > a :
    print('Os lados {},{},{} formam um triangulo'.format(a,b,c))
else:
    print('Os lados {},{},{} nao formam um triangulo'.format(a,b,c))
