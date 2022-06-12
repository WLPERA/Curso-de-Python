numero = cont = soma = 0
while numero!= 999:
    numero=int(input('Digite o numero desejado 999 para encerrar: '))
    if numero!=999:
        soma=soma+numero
        cont += 1
print('Foram digitados {} e a soma entre eles é {}:'.format(cont,soma))
