## deixar duas linhas em branco
def linhas(frase):
    print('~' * (len(frase)+4))
    print(f'  {frase}')
    print('~' * (len(frase)+4))

frase=str(input('Forneca a frase:'))
linhas(frase)



