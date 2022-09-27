#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário descobrir qual foi o número escolhido pelo computador.
# -O programa deverá escrever na tela se o usúario venceu ou perdeu.


from random import randint
from time import sleep
computador = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')

jogador = int(input('Em qual número eu pensei? '))
print('Processando o resultado...')
sleep(3)
if jogador == computador:
    print('Parabéns, Você venceu!!!')
else:
    print('Ganhei. Eu pensei no número {} e não no {}'.format(computador, jogador))
