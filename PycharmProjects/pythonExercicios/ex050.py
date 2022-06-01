soma=0
for n in range(1,7,1):
    numero = int(input('Digite um numero : '))
    if numero%2 == 0:
        soma+=numero
print('A soma final é {}'.format(soma))


