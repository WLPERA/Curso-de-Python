while True:
    numero = int(input('Tabuada de : '))
    if numero>0:
        for n in range(1,11,1):
            print('{} X {} = {}!'.format(numero, n, numero*n))
        print('-=' * 10)
    else:
        print('Acabou!')
        break



