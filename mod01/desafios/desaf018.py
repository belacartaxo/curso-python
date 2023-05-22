import math
print('=======DESAFIO 18=======')
num = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O valor do seno, cosseno e da tangente de ', end='')
print('{} é {:.3f}, {:.3f} e {:.3f}'.format(num, sen, cos, tan))
