lista = []
for c in range(0,5):
    n = int(input('Digite um valor:'))
    # checa se é o primeiro ou o ultimo
    if c==0 or n> lista[-1]:
        lista.append(n)
    else:
        # checa se  numero está no meio da lista
        pos = 0
        while pos < len(lista):
            if n<= lista[pos]:
                lista.insert(pos,n)
                break
            pos +=1

print('-='* 30)
print(f'Os valores digitados foram {lista}')


