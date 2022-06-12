tabela = ('Corinthians','Palmeiras','Atletico MG','Chapecoense','Vasco','Coritiba'
,'Sao Paulo','Flamengo','Botafogo','Cruzeiro', 'Gremio', 'Santos', 'Cuiaba', 'Atletico PR', 'Internacional'
,'Guarani', 'Fortaleza', 'Ceara', 'Vitoria', 'Bahia')

print(f'Os cinco primeiros do campeonato sao {tabela[:5]}')
print(f'Os cinco últimos do campeonato sao {tabela[-4:]}')
print(f'Os times em ordem alfabetica sao {sorted(tabela)}')
print('A posicao do Flamengo no campeonato é {}'.format(tabela.index('Flamengo')+1))
