##032: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

import calendar
ano = int(input('Digite um ano: '))
bis = ano / 4
if bis  == 0:
    print('Esse ano é bissexto'.format(bis))