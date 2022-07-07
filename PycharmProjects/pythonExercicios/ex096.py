## deixar duas linhas em branco

def area(largura,comprimento):
    calculo=largura*comprimento
    print(f'A área de um terreno {largura} x {comprimento} é {calculo} m2.')

print('-*' * 30)
print('Controle de Terrenos')
l=float(input('Forneca a largura:'))
c=float(input('Forneca o comprimento:'))
area(l,c)


