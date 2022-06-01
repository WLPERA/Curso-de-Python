
somadeidades=0;
homemmaisvelho=0;
mulheresmenores=0;
for i in range(0,4):
    nome = str(input("Digite o nome:"))
    sexo = str(input("Qual o sexo ?"))
    idade= int(input("Qual a idade ?"))
    somadeidades+=idade
    if sexo=='M' and idade>homemmaisvelho:
        homemmaisvelho=idade
    if sexo=='F' and idade<20:
        mulheresmenores=mulheresmenores+1

print('A media de idade do grupo é {} anos'.format(somadeidades/4))
print('O homem mais velho tem {} anos'.format(homemmaisvelho))
print('Temos  {} mulheres com menos de 20 anos'.format(mulheresmenores))