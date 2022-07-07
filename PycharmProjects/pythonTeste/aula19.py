## deixar duas linhas em branco

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

def contador(* num):
    for valor in num:
        print(valor)
# desempacotamento

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1a
# lista

titulo(' CURSO EM VÍDEO ')
titulo(' APRENDA PYTHON ')
titulo(' GUSTAVO GUANABARA ')

contador(2,3,3)
titulo(' parte 2 ')
contador(2,3,3,5,6,7)

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)
