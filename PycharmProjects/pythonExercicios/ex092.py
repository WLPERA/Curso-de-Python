from datetime import date
anoatual = date.today().year
funcionario = dict()
funcionario['nome'] = str(input('Nome do Funcionário: '))
funcionario['nascimento'] = int(input('Ano de Nascimento :'))
funcionario['ctps'] = int(input('CPTS (0 não tem): '))
if funcionario['ctps'] != 0:
    funcionario['anocontratacao'] = int(input('Ano de Contratação :'))
    funcionario['salario'] = float(input('Salário :'))
print(funcionario)
idade=anoatual-funcionario['nascimento']
print(f'O nome é igual {funcionario["nome"]}')
print(f'A Idade e igual {idade}')
if funcionario['ctps'] != 0:
    print(f'Ctps é igual {funcionario["ctps"]}')
    print(f'Contratação é igual {funcionario["anocontratacao"]}')
    print(f'Salário é igual {funcionario["salario"]}')
    print(f'Aposentadoria {funcionario["anocontratacao"]+35}')

