import random
ct=0
while True:
    numero = int(input('Digite um numero: '))
    computador = random.randint(1,10)
    ct += 1
    if (numero + computador) % 2 == 0:
        print(f'Você venceu  jogou {numero} e o computador {computador} total deu {numero+computador} par')
    else:
        print(f'Você perdeu jogou {numero} e o computador {computador} total deu {numero+computador} impar, tentou {ct} vezes')
        print('Acabou!')
        break

