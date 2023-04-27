print('=======DESAFIO 15=======')
km = int(input('Quantos km você percorreu? '))
dias = int(input('Por quantos dias você alugou o carro? '))
val = 0.15*km + 60*dias
print('O valor que você deve pagar é: R${:.2f}'.format(val))
