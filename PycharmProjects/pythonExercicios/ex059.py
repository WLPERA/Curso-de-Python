opcao =0 ;
while opcao!=5:
    valor1 = int(input('Favor Digite o primeiro valor: '))
    valor2 = int(input('Favor Digite o segundo valor: '))
    opcao = int(input('Selecione uma opcao 1->Soma 2-> multiplicacao 3-> maior, 4-> novos numeros, 5->encerrar'))
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