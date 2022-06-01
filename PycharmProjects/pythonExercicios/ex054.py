from datetime import date
anoatual = date.today().year

contagem=0
for i in range(0,7):
    ano=int(input("Qual o ano do Nascimento:"))
    if anoatual-ano>=21:
        contagem=contagem+1
print('Temos {} pessoas maiores de idade'.format(contagem))

