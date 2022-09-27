#:Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R#0,45 para viagens mais longas.

km = float(input(' Digite qual a distância da viajem em KM? '))

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
    print('O total da passagem será R${}'.format(preco))