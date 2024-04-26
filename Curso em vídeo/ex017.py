import math
cateto1 = int(input('Digite o primeiro cateto: '))
cateto2 = int(input('Digite o segundo cateto: '))
hip = math.hypot(cateto1, cateto2)
print('A hipotenusa dos 2 catetos é {}'.format(math.trunc(hip)))