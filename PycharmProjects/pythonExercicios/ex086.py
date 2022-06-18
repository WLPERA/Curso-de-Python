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
for l in range(0,3):
    for c in range(0,3):
        print(f'[{num[l] [c]}]',end='')
    print()