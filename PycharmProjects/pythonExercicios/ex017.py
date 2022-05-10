from math import sqrt
catetooposto = float(input('Cateto oposto:'))
catetoadjacente = float(input('Cateto adjacente:'))
hipotenusa = sqrt(pow(catetooposto,2)+pow(catetoadjacente,2))
print ('O cateto oposto {} e o cateto adjacente  {} formam a hipotenusa {}'.format(catetooposto,catetooposto,hipotenusa))