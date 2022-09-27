
#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#shuffle - embaralhar
import random

a1 = str(input('Aluno1: '))
a2 = str(input('Aluno2: '))
a3 = str(input('Aluno3 '))
a4 = str(input('Aluno4 '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
