
ficha = list()
while True:
    nome = str(input(f'Digite o Nome :'))
    nota1 = float(input(f'Digite a Primeira Nota :'))
    nota2 = float(input(f'Digite a Segunda Nota:'))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    # formatacao a direita e esquerda de cada campo {"No.":<4}{"NOME":<10}{"MEDIA":>8
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc] [0]} são {ficha[opc] [1]}')
        # ficha [opc] 0 -> traz o nome, ficha[opc] 1 -> traz as notas pois foi criada# uma sublista na linha 8
    print('<<< Volte Sempre >>>')


