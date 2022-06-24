jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input('Partidas Jogadas :'))
gols = list()
for c in range(1,jogador['partidas']+1):
    gols.append(int(input(f'Qual o numero de gols da partida {c}: ')))
jogador['gols'] = gols.copy()
print(jogador)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i,v in enumerate(jogador['gols']):
  print(f'    => Na partida {i}, fez {v} gols. ')



