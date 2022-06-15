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
print(f'Você Digitou {len(valores)} elementos.')
valores.sort(reverse=True)

print(f"Os valores digitados em forma decrescente foram {valores}")

if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 nao faz parte da lista')


