soma=0
cont=0
for n in range(1,7,1):
    numero = int(input('Digite o {} valor  : '.format(n)))
    if numero%2 == 0:
        soma+=numero
        cont +=1
print('Você informou {} numeros pares e a soma final é {}'.format(cont,soma))


