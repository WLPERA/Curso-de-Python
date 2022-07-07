from time import sleep

def maior(* param):
    ct=0
    maior=0
    for item in param:
        print(f'{item} ',end = '')
        sleep(1)
        ct+=1
        if item>maior:
            maior=item
    print(f'O Numero de Parametros passados foi : {ct}')
    print(f'O Maior item foi {maior}')
print('Analisando os valores passados :')
maior(10,0,2,5)
