nome = str(input('Digite o nome completo :')).upper().strip()
dividido = nome.split()
print ('O primeiro nome de {} é {}'.format(nome,dividido[0]))
print ('O ultimo nome de {} é {}'.format(nome,dividido[len(dividido)-1]))
