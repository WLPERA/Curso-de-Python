print('Gerador de PA')
print('-=' * 10)
primeirotermo=int(input('Digite o primeiro termo:'))
razao=int(input('Digite a razao:'))
termo = primeirotermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end='-> ')
        termo+=razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('ACABOU')
