expr = str(input('Digite a expressão:'))
pilha = []

for simb in expr:
    # faz a leitura da expressao e coloca os parenteses abertos numa pilha
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        # checa a pilha com parenteses abertos. Caso encontre tira um ) até zerar
        if len(pilha) >0 :
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) ==0 :
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
