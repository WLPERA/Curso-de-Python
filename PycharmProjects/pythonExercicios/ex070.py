print('-=' * 20)
print('Loja Super Baratao')
print('-=' * 20)
totalcompra = maioresque1000 = produtomaisbarato =0
nomeprodutomaisbarato=''
cont=0
while True:
    produto = str(input("Nome do produto ?")).upper()
    preco= int(input("Qual a preço ?"))
    totalcompra+=preco
    cont+=1
    if preco>=1000:
        maioresque1000+=1
    if cont==1:
        produtomaisbarato=preco
        nomeprodutomaisbarato=produto
    elif  preco<produtomaisbarato:
        produtomaisbarato=preco
        nomeprodutomaisbarato = produto
    continuar = str(input("Deseja Continuar [S/N]")).upper().strip()[0]
    if continuar == 'N':
        print(f'O total da compra foi  {totalcompra}')
        print(f'Temos {maioresque1000} produtos maiores que 1000')
        print(f'O produto mais barato foi {nomeprodutomaisbarato} que custa {produtomaisbarato}')
        break



