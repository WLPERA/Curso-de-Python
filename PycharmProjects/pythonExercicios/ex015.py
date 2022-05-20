km = float(input('Km percorridos ?'))
dias = int(input('Dias alugados?'))
preco = float(input('Preco :'))
valorapagar = km*dias*preco
print('O carro percorreu {} km por {} dia, total a pagar : {:.2f}!'.format(km,dias,valorapagar))
