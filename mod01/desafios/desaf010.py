print('=======DESAFIO 10=======')
n = float(input('Qual o valor que você deseja converter? R$'))
print('Você possui R${:.2f} que '.format(n), end='')
print('podem ser convertidos em US${:.2f}'.format(n/5.05))
