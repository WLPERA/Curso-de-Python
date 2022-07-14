from Ex112.utilidadescev import moeda
from Ex112.utilidadescev import dado

p = dado.leiaDinheiro("Digite o preço: ")
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(p,10,True)}')
