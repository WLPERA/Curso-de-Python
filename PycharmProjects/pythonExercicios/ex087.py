num = [[], [], []]
# uma lista com duas internas
valor = 0
for c in range(1,4):
    valor1=int(input(f'Digite o 1o. valor :'))
    valor2=int(input(f'Digite o 2o. valor :'))
    valor3=int(input(f'Digite o 3o. valor :'))
    num[0].append(valor1)
    num[1].append(valor2)
    num[2].append(valor3)

print('-=' * 30)
valorespares=0
terceiracoluna=0
maiorvalor=0
for l in range(0,3):
    for c in range(0,3):
        print(f'[{num[l] [c]}]',end='')
        if num[l] [c] % 2 == 0:
            valorespares += num[l] [c]
        if c==2:
            terceiracoluna += num[l] [c]
        if l==1:
            if num[l] [c] > maiorvalor:
                maiorvalor=num[l] [c]
    print()
print(f'A Soma dos valores pares é {valorespares}')
print(f'A Soma dos valores da terceira coluna sao {terceiracoluna}')
print(f'o maior valor da segunda linha é  {maiorvalor}')