def fatorial(valor,show=False):
    """
    --> Calcula o Fatorial de um número.
    :param valor: O número a ser calculado
    :param show: (opcional) Mostrar o não a conta
    :return: O valor do Fatorial de um numero n
    """
    c = valor
    f = 1
    if show:
        print('Calculando {}!='.format(valor), end= ' ')
    while c > 0:
        if show:
            print('{} '.format(c), end = ' ')
            print('x ' if c > 1 else '= ',end = '')
        f *= c
        c -= 1
    return f
valor=5
f=fatorial(valor)
print('O fatorial de {} é {}'.format(valor,f))
help(fatorial)