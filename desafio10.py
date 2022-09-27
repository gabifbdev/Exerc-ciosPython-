real = float(input('Insira quanto você tem na carteira R$: '))
dolar = real / 5.24

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))