
maiorpeso=0
menorpeso=0
for i in range(0,5):
    peso=int(input("Qual o Peso:"))
    if i == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso>maiorpeso:
            maiorpeso=peso
        if peso< menorpeso:
            menorpeso=peso
print('O maior peso lido é {} !!'.format(maiorpeso))
print('O menor peso lido é {} !!'.format(menorpeso))

