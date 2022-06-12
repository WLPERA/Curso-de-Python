numero = maior = menor = soma =0
fim='S'
cont=1
while fim=='S':
    numero=int(input('Digite um numero: '))
    soma=numero+soma
    if numero>maior:
        maior=numero
    if numero<menor or cont!=1:
        menor=numero
    fim = str(input('Deseja continuar ? ')).upper().strip()[0]
    cont+=1

print('Foram digitados {} e a soma entre eles é {}:'.format(cont-1,soma))
print('A media é {}, o maior {} e a menor {}:'.format((soma/(cont-1)),maior,menor))
