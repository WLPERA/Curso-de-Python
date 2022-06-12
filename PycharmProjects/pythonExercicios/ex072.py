extenso = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um numero entre 0 e 20:'))
    if numero>=0 and numero<20:
        break
print(f'O numero {numero} por extenso é {extenso[numero]}')
