print('=======DESAFIO 11=======')
b = int(input('Qual é a largura da parede(m)? '))
h = int(input("Qual é a altura da parede(m)? "))
s = b*h
print('A área da parede é {}m^2, '.format(s), end='')
print('logo será necessário {} litros de tinta para pinta-la.'.format(s/2))
