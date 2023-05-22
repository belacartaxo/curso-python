import random
print('=======DESAFIO 19=======')
nome1 = input(('1° aluno: '))
nome2 = input(('2° aluno: '))
nome3 = input(('3° aluno: '))
nome4 = input(('4° aluno: '))
escolhido = random.choice([nome1, nome2, nome3, nome4])
print('O aluno escolhido foi: {}'.format(escolhido))
