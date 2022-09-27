#Escreva um programa que leia a velocidade de um carro.
# -Se ele ultrapassar 80Km/, mostre uma mensagem dizendo que ele foi multado.
# -A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade atual do carro em KM: '))

multa = (vel - 80)
total = multa * 7
if vel > 80:
    print("Você foi multado!!!! Excedeu o limite permitido que é de 80km/h. Você deverá pagar uma multa de R$ {} reais".format(total))
else:
    print('Tenha um excelente dia. Dirija com segurança!!')
