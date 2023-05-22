import math
print('=======DESAFIO 17=======')
co = int(input('Digite o valor do cateto oposto: '))
cs = int(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(co, cs)
print('A hipotenusa correspondentes aos cossenos ', end='')
print('{} e {} é {}'.format(co, cs, hip))
