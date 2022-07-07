def leiaint(msg):
    while True:
        numero=str(input(f'{msg}'))
        if numero.isnumeric():
           break
        else:
            print('\033[0:31mErro !!! Digite um número inteiro válido :\033[m')
    return numero

n=leiaint('Digite um Número:')
print(f'Você acabou de digitar o numero {n}')
