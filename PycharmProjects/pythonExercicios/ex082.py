valores = list()
while True:
    valores.append(int(input('Digite um valor:')))
    while True:
        continua = str(input('Deseja continuar [S/N]:')).upper()
        if continua in 'SN':
            break
    if continua == 'N':
        break
print('-=' * 30)

pares = list()
impares = list()

for numero in valores:
    if numero % 2==0:
        pares.append(numero)
    else:
        impares.append(numero)

print('-=' * 30)
print(f'A lista digitada foi {valores}')
print(f'Os numeros pares são {pares}')
print(f'Os numeros impares são {impares}')






