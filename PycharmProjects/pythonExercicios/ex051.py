primeirotermo=int(input('Digite o primeiro termo:'))
razao=int(input('Digite a razao:'))
decimo = primeirotermo + (10 -1) * razao
for n in range(primeirotermo,decimo + razao,razao):
    print('{}'.format(n), end='-> ')
print('ACABOU')




