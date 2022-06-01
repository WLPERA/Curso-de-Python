cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

casa = float(input('Favor digite o valor da casa:'))
salario = float(input('Favor digite o valor do salario:'))
anos = int(input('Favor digite em quantos anos será paga:'))
prestacao = float(casa/(anos*12))
porcentagem = float((prestacao*100)/salario)

if porcentagem<31:
    print('Emprestimo aprovado. A casa custa {:.2f} e financiada por {} anos,'
          ' tera prestacao de {:.2f}, correspondente a {}{:.2f}{} % de seu salario'
          .format(casa,anos,prestacao,cores['azul'],porcentagem,cores['limpa'],salario))
elif porcentagem>=30:
    print('Emprestimo negado. A casa custa {:.2f} e financiada por {} anos,'
          ' tera prestacao de {:.2f}, correspondente a {}{:.2f}{} % de seu salario'
          .format(casa, anos, prestacao, cores['amarelo'], porcentagem, cores['limpa'], salario))

    #if (a+b) > c and (a+c) > b and (b+c) > a :
#    print('Os lados {}{}{},{},{} formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
#else:
#    print('Os lados {}{}{},{},{} nao formam um triangulo'.format(cores['azul'],a,cores['limpa'],b,c))
