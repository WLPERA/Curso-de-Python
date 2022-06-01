numero=int(input('Digite o numero:'))
tot = 0
for i in range(1,numero+1):
    if numero % i ==0:
        print('\033[33m',end='')
        tot += 1
    else:
        print('\033[31m',end='')
    print('{} '.format(i),end='')
print('\n\033[mO numero {} foi divisível {} vezes'.format(numero,tot))
if tot==2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele nao é primo!')






