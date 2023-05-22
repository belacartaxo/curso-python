import random
print('=======DESAFIO 20=======')
nome1 = input(('1° aluno: '))
nome2 = input(('2° aluno: '))
nome3 = input(('3° aluno: '))
nome4 = input(('4° aluno: '))
ordem = [nome1, nome2, nome3, nome4]
random.shuffle(ordem)
print('O aluno escolhido foi: {}'.format(ordem))
