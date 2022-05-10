import math
angulo = float(input('Angulo:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print ('Dado o angulo {}, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo,seno,cosseno,tangente))