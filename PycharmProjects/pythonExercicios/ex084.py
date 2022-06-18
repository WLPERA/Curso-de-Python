galera = list()
dado = list()
ct=0
maiorpeso=menorpeso=0
while True:    
    dado.append(str(input('Nome: ')))
    dado.append(int(input("Peso: ")))
    galera.append(dado[:])
    ct+=1
    if ct==1:
        maiorpeso=menorpeso=dado[1]
    else:
        if dado[1]<menorpeso:
            menorpeso=dado[1]
        if dado[1]>maiorpeso:
            maiorpeso=dado[1]
    dado.clear()
    continua=str(input('Deseja Continuar S/N :')).upper()
    if continua == 'N':
        break
print(f'Foram digitadas {ct} pessoas !')
for p in galera:
    if p[1] == maiorpeso:
        print(f'{p[0]} tem o maior peso com {p[1]} kilos', end=' ')
    if p[1] == menorpeso:
        print(f'{p[0]} tem o menor peso com {p[1]} kilos', end=' ')
