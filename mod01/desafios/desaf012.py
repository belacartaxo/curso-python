print('=======DESAFIO 12=======')
n = float(input('Qual é o valor do produto? R$'))
print('O valor do produto é R${:.2f}, e'.format(n), end='')
print(' com 5% de desconto ele sai por R${:.2f}'.format(n*95/100))
