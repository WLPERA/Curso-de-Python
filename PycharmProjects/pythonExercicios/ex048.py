total=0
cont=0
for n in range(1,501,2):
    if n%3 == 0:
        total +=n
        cont +=1
print('A soma de todos os {} valores multiplos de 3 é : {}'.format(cont,total))


