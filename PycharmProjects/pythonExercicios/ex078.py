valores = list()
maior=menor=0
for cont in range (0,5):
    valores.append(int(input('Digite um valor:')))
    if cont==0:
        maior=menor=valores[cont]
    else:
        if valores[cont]>maior:
            maior=valores[cont]
        if valores[cont]<menor:
            menor=valores[cont]

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posicoes ',end='')
for c,v in enumerate(valores):
    if maior==v:
        print(f'{c}... ',end='')
print()
print(f'O menor valor digitado foi {menor} nas posicoes ',end='')
for c,v in enumerate(valores):
    if menor==v:
        print(f'{c}... ',end='')
print()
