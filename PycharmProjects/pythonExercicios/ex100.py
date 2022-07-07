from random import randint

def sorteia(lista):
    for cont in range(0,5):
        lista.append(randint(1,10))

def pares(numeros):
    somapar=0
    for i in numeros:
        if i%2==0:
            somapar+=i
    print(f'A soma dos valores pares são {somapar}')

numeros = list()
sorteia(numeros)
print(numeros)
pares(numeros)

