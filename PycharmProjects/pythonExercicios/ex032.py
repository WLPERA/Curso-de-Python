ano = int(input('Favor Digite o ano:'))
resto  = ano % 4
if resto==0:
    print ('o ano {} é Bissexto'.format(ano))
else:
        print('o ano {} não é Bissexto'.format(ano))

