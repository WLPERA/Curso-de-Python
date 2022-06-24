from random import randint
from time import sleep
from operator import itemgetter
# item getter => busca a posicao no dicionario 0=nome do jogador, 1 valor randomico
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }
ranking = list()
print('Valores Sorteados:')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking=sorted(jogo.items(), key=itemgetter(1),reverse=True)
print('-=' * 30)
print(' == Ranking dos Jogadores ==')

for i,v in enumerate(ranking):
    print(f'{i+1}.o lugar : {v[0]} com {v[1]}.')
    sleep(1)
