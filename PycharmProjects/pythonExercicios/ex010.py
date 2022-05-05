valor = int(input('Valor em reais ?'))
cotacao = float(input('Cotacao do dolar ?'))
conversao = valor/cotacao

print('O valor {} convertido por {}, é {:.2f}'.format(valor,cotacao,conversao))

