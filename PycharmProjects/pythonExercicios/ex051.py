primeirotermo=int(input('Digite o primeiro termo:'))
razao=int(input('Digite a razao:'))
calculo=primeirotermo
for n in range(1,10):
    print('O termo {} da progressao é {}'.format(n,calculo))
    calculo+=(calculo+razao)-primeirotermo





