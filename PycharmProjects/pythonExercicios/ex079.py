valores = list()
while True:
    valor = int(input('Digite um valor:'))

    if valor in valores:
        print('Valor duplicado nao vou adicionar...')
    else:
        valores.append(valor)

    while True:
        continua = str(input('Deseja continuar [S/N]:')).upper()
        if continua in 'SN':
            break
    if continua == 'N':
        break

print(f'Os valores digitados foram {sorted(valores)}')


