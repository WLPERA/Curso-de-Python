opcao =0 ;
while opcao!=5:
    valor1 = int(input('Favor Digite o primeiro valor: '))
    valor2 = int(input('Favor Digite o segundo valor: '))
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Menor
    [5] Sair do programa
    ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao==1:
        print('A opcao selecionada foi {} e a soma é {}'.format(opcao,valor1+valor2))
    elif opcao == 2:
        print('A opcao selecionada foi {} e a multiplicacao é {}'.format(opcao,valor1*valor2))
    elif opcao ==3 :
        if valor1>valor2:
            print('A opcao selecionada foi {} e o maior valor é {}'.format(opcao, valor1))
        else:
            print('A opcao selecionada foi {} e o maior valor é {}'.format(opcao, valor2))
print('Fim do programa')