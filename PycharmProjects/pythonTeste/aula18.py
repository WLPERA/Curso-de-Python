pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
del pessoas['sexo']
pessoas['peso']= 98.5
pessoas['nome'] = 'Leandro'
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k,v in pessoas.items():
    print(f'{k} = {v}')
