sexo = ''
while sexo!='M' and sexo!='F':
    sexoinformado = str(input('Digite o sexo :')).upper()
    if sexoinformado=='M' or sexoinformado=='F':
        print('O sexo informado foi {}'.format(sexoinformado))
        break