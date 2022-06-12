maiores18 = homens = mulheresmenores20 =0
while True:
    sexo = str(input("Qual o sexo ?")).upper().strip()[0]
    idade= int(input("Qual a idade ?"))
    if idade>18:
        maiores18+=1
    if sexo=='M':
        homens+=1
    elif idade <20:
        mulheresmenores20+=1
    continuar = str(input("Deseja Continuar [S/N]")).upper().strip()[0]
    if continuar == 'N':
        print(f'Foram digitados {maiores18} com mais de 18 anos, sendo {homens} homens e {mulheresmenores20} mulheres com menos de 20 anos ')
        break
