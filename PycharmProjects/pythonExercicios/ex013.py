salario = int(input('Salario ?'))
aumento = int(input('Aumento?'))
novosalario = (salario + salario*( aumento/100))
print('O Salario {} com {} % de aumento fica {} '.format(salario,aumento,novosalario))
