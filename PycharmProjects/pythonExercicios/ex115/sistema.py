from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome :'))
        idade = leiaint('Idade :')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até Logo')
        break
    else:
        cabecalho('Erro ! Digite uma opção válida !')