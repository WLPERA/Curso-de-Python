numero = (  int(input('Digite um numero: ')),
            int(input('Digite um numero: ')),
            int(input('Digite um numero: ')),
            int(input('Digite um numero: ')))
print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.count(3)+1} posicao')
else:
    print(f'O valor 3 nao apareceu em nenhuma posicao')
for n in numero:
    if n%2 ==0:
        print(n,end=' ')


