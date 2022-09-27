#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#choice - escolher
import random
a1 = str(input('Aluno1: '))
a2 = str(input('Aluno2: '))
a3 = str(input('Aluno3 '))
a4 = str(input('Aluno4 '))
lista = [a1, a2, a3, a4]
print('O aluno escolhido é o {}:'.format(random.choice(lista)))