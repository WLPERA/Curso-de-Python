from datetime import date
ano = int(input('Favor Digite o ano: 0 para analisar o ano atual :'))
if ano ==0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 !=0 or ano % 400 ==0:
    print ('o ano {} é Bissexto'.format(ano))
else:
        print('o ano {} não é Bissexto'.format(ano))

