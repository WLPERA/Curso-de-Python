def voto(ano):
    # importacao funciona somente dentro da funcao
    from datetime import date
    anoatual = date.today().year
    if anoatual-ano > 65:
        return 'Voto Opcional !'
    elif anoatual-ano > 18:
        return 'Voto Obrigatorio'
    else:
        return 'Voto Negado'

ano = int(input('Digite o ano de Nascimento: '))
print(voto(ano))

