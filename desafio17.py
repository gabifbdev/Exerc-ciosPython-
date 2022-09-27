#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.



'''oposto = float(input('Digite o comprimento do cateto oposto:'))
adjacente = float(input('Digite o comprimento do cateto adjacente:'))
x = (oposto ** 2 + adjacente ** 2) **(1/2)

print('O comprimento da hipotenusa é {}'.format(x))'''


from math import hypot

oposto = float(input('Digite o comprimento do cateto oposto:'))
adjacente = float(input('Digite o comprimento do cateto adjacente:'))
x = hypot(oposto, adjacente)

print('O comprimento da hipotenusa é {}'.format(x))
