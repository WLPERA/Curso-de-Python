salario = float(input('Favor digite o salário do funcionario:'))

if salario >= 1250:
    reajuste = salario * 1.1
    print('O salario {} reajustado em 10% é {:.2f}'.format(salario,reajuste))
else:
    reajuste = salario * 1.15
    print('O salario {} reajustado em 15% é {:.2f}'.format(salario, reajuste))