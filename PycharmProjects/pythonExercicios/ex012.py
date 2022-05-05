preco = int(input('Preço de um produto ?'))
desconto = int(input('Desconto?'))
precofinal = (preco - preco*( desconto/100))
print('O preço {} com {} % de desconto sai {} '.format(preco,desconto,precofinal))