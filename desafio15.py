#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km foram rodados?'))
dias = int(input('Quantos dias alugados?'))
rodado = 0.15
precodia = 60
precoKm = rodado * km
alugueldias = dias * precodia
precoAluguel = precoKm + alugueldias

print('O valor total do aluguel será de {}'.format(precoAluguel))