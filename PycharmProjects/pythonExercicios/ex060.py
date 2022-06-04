valor = int(input('Digite um numero:'))
c = valor
f = 1
print('Calculando {}!='.format(valor), end= '')
while c > 0:
    print('{} '.format(c), end = ' ')
    print('x ' if c > 1 else '= ',end = '')
    f *= c
    c -= 1
print('O fatorial de {} é {}'.format(valor,f))